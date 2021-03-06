"""
 This is the basis for an elasticsearch 1.x backend I've cobbled together and am continuing 
 to refine and test for use. It's based on haystack main's version as of:
    - https://github.com/toastdriven/django-haystack/blob/cbb72b3253404ba21e20860f620774f7b7b691d0/haystack/backends/elasticsearch_backend.py
 But with @HonzaKral and @davedash's work to make the backend behave more like an ES user would expect with regard to doc types:
    - https://github.com/toastdriven/django-haystack/pull/921

 I also made a number of changes:
    - I fixed bugs that I found in #921 (mostly related to mapping synchronization issues), 
      all of which I wrote up as comments on #921
    - I'm using the non-django six library (because I happen to be running this on Django 1.3, 
      but you can import django's six instead if you want. Should be drop-in)
    - I translate "score" in order_by clauses to "_score" cause it made some code I share 
      with a solr backend easier.
 
 At this point my testing has been pretty broad, but not very deep. I think index updates and 
 rebuilds work well, I'm fairly confident that the mapping synchronization works better than
 any elasticsearch backend implementation I've found in the haystack commit tree. The models
 I tested with are fairly wide and complex, but I'm sure didn't cover every data type.
 Also, in my testing I'm running against an unmodified Haystack v2.0.0, elasticsearch 1.4.0,
 and Django 1.3.X, but it ought to work in later versions of all. I'm not positive that 
 I haven't broken py3 compatibility but I tried not to violate it while making changes.
 
 ALSO: List above may no longer be complete. Plus I do kooky things in here like ignore mapping 
 errors if I have a unit testing flag in settings.
 
 If you use this and find issues, please let me know!
"""
from __future__ import unicode_literals
import datetime
import re
import warnings

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.loading import get_model
import six
import haystack
from haystack.backends import BaseEngine, BaseSearchBackend, BaseSearchQuery, log_query
from haystack.constants import DJANGO_CT, DJANGO_ID, DEFAULT_OPERATOR
from haystack.exceptions import MissingDependency, MoreLikeThisError
from haystack.inputs import PythonData, Clean, Exact, Raw
from haystack.models import SearchResult
from haystack.utils import log as logging

try:
    import elasticsearch
    from elasticsearch.helpers import bulk_index
except ImportError:
    raise MissingDependency("The 'elasticsearch' backend requires the installation of 'elasticsearch'. Please refer to the documentation.")


DATETIME_REGEX = re.compile(
    r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T'
    r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.\d+)?$')


class ElasticsearchSearchBackend(BaseSearchBackend):
    # Word reserved by Elasticsearch for special use.
    RESERVED_WORDS = (
        'AND',
        'NOT',
        'OR',
        'TO',
    )

    # Characters reserved by Elasticsearch for special use.
    # The '\\' must come first, so as not to overwrite the other slash replacements.
    RESERVED_CHARACTERS = (
        '\\', '+', '-', '&&', '||', '!', '(', ')', '{', '}',
        '[', ']', '^', '"', '~', '*', '?', ':', '/',
    )

    # Settings to add an n-gram & edge n-gram analyzer.
    DEFAULT_SETTINGS = {
        'settings': {
            "analysis": {
                "analyzer": {
                    "ngram_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["haystack_ngram", "lowercase"]
                    },
                    "edgengram_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["haystack_edgengram", "lowercase"]
                    },
                    "case_insensitive_phrase": {
                        "filter": ["lowercase",],
                        "tokenizer": "keyword",
                    },
                },
                "tokenizer": {
                    "haystack_ngram_tokenizer": {
                        "type": "nGram",
                        "min_gram": 3,
                        "max_gram": 15,
                    },
                    "haystack_edgengram_tokenizer": {
                        "type": "edgeNGram",
                        "min_gram": 1,
                        "max_gram": 25,
                        "side": "front"
                    }
                },
                "filter": {
                    "haystack_ngram": {
                        "type": "nGram",
                        "min_gram": 3,
                        "max_gram": 15
                    },
                    "haystack_edgengram": {
                        "type": "edgeNGram",
                        "min_gram": 1,
                        "max_gram": 25
                    }
                }
            }
        }
    }

    def __init__(self, connection_alias, **connection_options):
        super(ElasticsearchSearchBackend, self).__init__(connection_alias, **connection_options)

        if 'URL' not in connection_options:
            raise ImproperlyConfigured("You must specify a 'URL' in your settings for connection '%s'." % connection_alias)

        if 'INDEX_NAME' not in connection_options:
            raise ImproperlyConfigured("You must specify a 'INDEX_NAME' in your settings for connection '%s'." % connection_alias)

        self.conn = elasticsearch.Elasticsearch(connection_options['URL'], timeout=self.timeout, 
                                                **connection_options.get('KWARGS', {}))
        self.index_name = connection_options['INDEX_NAME']
        self.log = logging.getLogger('haystack')
        self.setup_complete = False
        self.existing_mapping = {}
        self.fail_on_mapping_merge_issue = connection_options.get('FAIL_ON_MAPPING_MERGE_ISSUE', False)

    def setup(self):
        """
        Defers loading until needed.
        """
        # Get the existing mapping & cache it. We'll compare it during the
        # ``update`` & if it doesn't match, we'll put the new mapping.
        try:
            raw_mapping_result = self.conn.indices.get_mapping(index=self.index_name)
            self.existing_mapping = raw_mapping_result[self.index_name]['mappings']
        except (elasticsearch.NotFoundError, KeyError):
            # NotFoundError means the doc_type isn't in the index yet
            # KeyError means the index doesn't exist yet
            pass

        mappings_to_put = {}

        unified_index = haystack.connections[self.connection_alias].get_unified_index()
        
        # Sigh... https://github.com/toastdriven/django-haystack/pull/851
        if not unified_index._built:
            unified_index.build()

        # Get mappings for all ElasticSearch types/models
        for model, index in unified_index.indexes.items():
            es_type = self.get_es_type(index)

            self.content_field_name, field_mapping = self.build_schema(index.fields)

            # construct whole mapping for the es type:
            current_mapping = {
                es_type: {
                    'properties': field_mapping,
                    '_boost': {
                        'name': 'boost',
                        'null_value': 1.0
                    }
                }
            }

            if current_mapping[es_type] != self.existing_mapping.get(es_type, {}):
                mappings_to_put.update(current_mapping)

        if not self.existing_mapping or mappings_to_put:

            # Make sure the index is there first, ignore 400 - index already created
            self.conn.indices.create(index=self.index_name, body=self.DEFAULT_SETTINGS, ignore=400)

            for es_type, mapping in mappings_to_put.items():
                try:
                    # create and store the mappings                
                    self.conn.indices.put_mapping(index=self.index_name, doc_type=es_type, body={es_type: mapping})
                    self.existing_mapping[es_type] = mapping
                except elasticsearch.TransportError as e:
                    if not getattr(settings, 'UNIT_TESTING', False):
                        # don't care about this error in unit tests
                        self.log.error("Failed to merge mapping to Elasticsearch: %s\nMapping attempted: %s", e, mapping)
                    if self.fail_on_mapping_merge_issue:
                        raise
        
        self.setup_complete = True

    def get_es_type(self, index_or_model):
        """
        Get the ElasticSearch document 'type' that is bound to a given
        index/model.
        """
        if not hasattr(index_or_model, '_meta'):
            index_or_model = index_or_model.get_model()

        return index_or_model._meta.db_table

    def get_type_and_id(self, obj_or_string):
        """
        Return a tuple of document type and document id given an object or string
        reprsenting an object.
        """
        if hasattr(obj_or_string, '_meta'):
            doc_id = '.'.join((obj_or_string._meta.app_label, obj_or_string._meta.module_name, str(obj_or_string.pk)))
            doc_type = self.get_es_type(obj_or_string)
        else:
            doc_id = obj_or_string
            doc_type = self.get_es_type(get_model(*obj_or_string.split('.')[:2]))
        return doc_type, doc_id

    def update(self, index, iterable, commit=True):
        if not self.setup_complete:
            try:
                self.setup()
            except elasticsearch.TransportError as e:
                if not self.silently_fail:
                    raise

                self.log.error("Failed to add documents to Elasticsearch: %s", e)
                return

        prepped_docs = []

        for obj in iterable:
            prepped_data = index.full_prepare(obj)
            final_data = {}

            # Convert the data to make sure it's happy.
            for key, value in prepped_data.items():
                final_data[key] = self._from_python(value)
            final_data['_type'], final_data['_id'] = self.get_type_and_id(obj)

            del final_data['id']

            prepped_docs.append(final_data)

        bulk_index(self.conn, prepped_docs, index=self.index_name)

        if commit:
            self.conn.indices.refresh(index=self.index_name)

    def remove(self, obj_or_string, commit=True):
        doc_type, doc_id = self.get_type_and_id(obj_or_string)

        if not self.setup_complete:
            self.setup()

        try:
            self.conn.delete(index=self.index_name, doc_type=doc_type, id=doc_id, ignore=404)

            if commit:
                self.conn.indices.refresh(index=self.index_name)
        except elasticsearch.TransportError as e:
            if not self.silently_fail:
                raise

            self.log.error("Failed to remove document '%s' from Elasticsearch: %s", doc_id, e)

    def clear(self, models=[], commit=True):
        # We actually don't want to do this here, as mappings could be
        # very different.
        # if not self.setup_complete:
        #     self.setup()

        try:
            if not models:
                self.conn.indices.delete(index=self.index_name, ignore=404)
                self.setup_complete = False
                self.existing_mapping = {}
            else:

                models_to_delete = [self.get_es_type(m) for m in models]
                for m in models_to_delete:
                    try:
                        self.conn.delete_by_query(self.index_name, doc_type=m, body={'query':{'match_all': {}}})
                    except elasticsearch.TransportError as e:
                        self.log.warn("Clear failed for %s-%s. Probably it's missing - %s" % (self.index_name, m, e))

                    # No longer deleting mapping here cause it causes nasty problems
                    # self.conn.indices.delete_mapping(index=self.index_name, doc_type=m, ignore=404)
                    # if m in self.existing_mapping:
                    #     del self.existing_mapping[m]

                if commit:
                    self.conn.indices.refresh(index=self.index_name, ignore=404)

        except elasticsearch.TransportError as e:
            if not self.silently_fail:
                raise

            if models:
                self.log.error("Failed to clear Elasticsearch index of models '%s': %s", ','.join(models_to_delete), e)
            else:
                self.log.error("Failed to clear Elasticsearch index: %s", e)

    def build_models_list(self):
        """
        overridden here because we need to use self.get_es_type()
        """
        from haystack import connections
        models = []

        for model in connections[self.connection_alias].get_unified_index().get_indexed_models():
            models.append(self.get_es_type(model))

        return models

    def build_search_kwargs(self, query_string, sort_by=None, start_offset=0, end_offset=None,
                            fields='', highlight=False, facets=None,
                            date_facets=None, query_facets=None,
                            narrow_queries=None, spelling_query=None,
                            within=None, dwithin=None, distance_point=None,
                            models=None, limit_to_registered_models=None,
                            result_class=None):
        index = haystack.connections[self.connection_alias].get_unified_index()
        content_field = index.document_field

        if query_string == '*:*':
            kwargs = {
                'query': {
                    "match_all": {}
                },
            }
        else:
            kwargs = {
                'query': {
                    'query_string': {
                        'default_field': content_field,
                        'default_operator': DEFAULT_OPERATOR,
                        'query': query_string,
                        'analyze_wildcard': True,
                        'auto_generate_phrase_queries': True,
                    },
                },
            }

        # so far, no filters
        filters = []

        if fields:
            kwargs['fields'] = list(fields)

        if sort_by is not None:
            order_list = []
            for field, direction in sort_by:
                if field == 'distance' and distance_point:
                    # Do the geo-enabled sort.
                    lng, lat = distance_point['point'].get_coords()
                    sort_kwargs = {
                        "_geo_distance": {
                            distance_point['field']: [lng, lat],
                            "order": direction,
                            "unit": "km"
                        }
                    }
                else:
                    if field == 'distance':
                        warnings.warn("In order to sort by distance, you must call the '.distance(...)' method.")

                    # Regular sorting.
                    ## TODO: From Phill, consider the change we'd picked from another bug:
                    ## sort_kwargs = {field: {'order': direction, 'missing' : '_last' , 'ignore_unmapped' : True}}
                    ## (it mattered when sorting on fields that didn't exist on all models)

                    sort_kwargs = {field: {'order': direction}}

                order_list.append(sort_kwargs)

            kwargs['sort'] = order_list

        # From/size offsets don't seem to work right in Elasticsearch's DSL. :/
        # if start_offset is not None:
        #     kwargs['from'] = start_offset

        # if end_offset is not None:
        #     kwargs['size'] = end_offset - start_offset

        if highlight is True:
            kwargs['highlight'] = {
                'fields': {
                    content_field: {'store': 'yes'},
                }
            }

        if self.include_spelling:
            kwargs['suggest'] = {
                'suggest': {
                    'text': spelling_query or query_string,
                    'term': {
                        # Using content_field here will result in suggestions of stemmed words.
                        'field': '_all',
                    },
                },
            }

        if narrow_queries is None:
            narrow_queries = set()

        if facets is not None:
            kwargs.setdefault('facets', {})

            for facet_fieldname, extra_options in facets.items():
                facet_options = {
                    'terms': {
                        'field': facet_fieldname,
                        'size': 100,
                    },
                }
                # Special cases for options applied at the facet level (not the terms level).
                if extra_options.pop('global_scope', False):
                    # Renamed "global_scope" since "global" is a python keyword.
                    facet_options['global'] = True
                if 'facet_filter' in extra_options:
                    facet_options['facet_filter'] = extra_options.pop('facet_filter')
                facet_options['terms'].update(extra_options)
                kwargs['facets'][facet_fieldname] = facet_options

        if date_facets is not None:
            kwargs.setdefault('facets', {})

            for facet_fieldname, value in date_facets.items():
                # Need to detect on gap_by & only add amount if it's more than one.
                interval = value.get('gap_by').lower()

                # Need to detect on amount (can't be applied on months or years).
                if value.get('gap_amount', 1) != 1 and not interval in ('month', 'year'):
                    # Just the first character is valid for use.
                    interval = "%s%s" % (value['gap_amount'], interval[:1])

                kwargs['facets'][facet_fieldname] = {
                    'date_histogram': {
                        'field': facet_fieldname,
                        'interval': interval,
                    },
                    'facet_filter': {
                        "range": {
                            facet_fieldname: {
                                'from': self._from_python(value.get('start_date'), for_query=True),
                                'to': self._from_python(value.get('end_date'), for_query=True),
                            }
                        }
                    }
                }

        if query_facets is not None:
            kwargs.setdefault('facets', {})

            for facet_fieldname, value in query_facets:
                kwargs['facets'][facet_fieldname] = {
                    'query': {
                        'query_string': {
                            'query': value,
                        }
                    },
                }

        if limit_to_registered_models is None:
            limit_to_registered_models = getattr(settings, 'HAYSTACK_LIMIT_TO_REGISTERED_MODELS', True)

        if models and len(models):
            model_choices = [self.get_es_type(model) for model in models]
        elif limit_to_registered_models:
            # Using narrow queries, limit the results to only models handled
            # with the current routers.
            model_choices = self.build_models_list()
        else:
            model_choices = []

        if len(model_choices) > 0:

            if narrow_queries is None:
                narrow_queries = set()

            # we could put these in the url but it's equivalent to the terms filter which is easier
            filters.append({"terms": {'_type': model_choices}})

        for q in narrow_queries:
            filters.append({
                'fquery': {
                    'query': {
                        'query_string': {
                            'query': q
                        },
                    },
                    '_cache': True,
                }
            })

        if within is not None:
            from haystack.utils.geo import generate_bounding_box

            ((south, west), (north, east)) = generate_bounding_box(within['point_1'], within['point_2'])
            within_filter = {
                "geo_bounding_box": {
                    within['field']: {
                        "top_left": {
                            "lat": north,
                            "lon": west
                        },
                        "bottom_right": {
                            "lat": south,
                            "lon": east
                        }
                    }
                },
            }
            filters.append(within_filter)

        if dwithin is not None:
            lng, lat = dwithin['point'].get_coords()
            dwithin_filter = {
                "geo_distance": {
                    "distance": dwithin['distance'].km,
                    dwithin['field']: {
                        "lat": lat,
                        "lon": lng
                    }
                }
            }
            filters.append(dwithin_filter)

        # if we want to filter, change the query type to filteres
        if filters:
            kwargs["query"] = {"filtered": {"query": kwargs.pop("query")}}
            if len(filters) == 1:
                kwargs['query']['filtered']["filter"] = filters[0]
            else:
                kwargs['query']['filtered']["filter"] = {"bool": {"must": filters}}

        return kwargs

    @log_query
    def search(self, query_string, **kwargs):
        if len(query_string) == 0:
            return {
                'results': [],
                'hits': 0,
            }

        if not self.setup_complete:
            self.setup()

        search_kwargs = self.build_search_kwargs(query_string, **kwargs)
        search_kwargs['from'] = kwargs.get('start_offset', 0)

        order_fields = set()
        for order in search_kwargs.get('sort', []):
            for key in order.keys():
                order_fields.add(key)

        geo_sort = '_geo_distance' in order_fields

        end_offset = kwargs.get('end_offset')
        start_offset = kwargs.get('start_offset', 0)
        if end_offset is not None and end_offset > start_offset:
            search_kwargs['size'] = end_offset - start_offset

        try:
            raw_results = self.conn.search(body=search_kwargs, index=self.index_name)
        except elasticsearch.TransportError as e:
            if not self.silently_fail:
                raise

            self.log.error("Failed to query Elasticsearch using '%s': %s", query_string, e)
            raw_results = {}

        return self._process_results(raw_results,
            highlight=kwargs.get('highlight'),
            result_class=kwargs.get('result_class', SearchResult),
            distance_point=kwargs.get('distance_point'), geo_sort=geo_sort)

    def more_like_this(self, model_instance, additional_query_string=None,
                       start_offset=0, end_offset=None, models=None,
                       limit_to_registered_models=None, result_class=None, **kwargs):
        from haystack import connections

        if not self.setup_complete:
            self.setup()

        # Deferred models will have a different class ("RealClass_Deferred_fieldname")
        # which won't be in our registry:
        model_klass = model_instance._meta.concrete_model

        index = connections[self.connection_alias].get_unified_index().get_index(model_klass)
        field_name = index.get_content_field()
        params = {}

        if start_offset is not None:
            params['search_from'] = start_offset

        if end_offset is not None:
            params['search_size'] = end_offset - start_offset

        doc_type, doc_id = self.get_type_and_id(model_instance)

        try:
            raw_results = self.conn.mlt(index=self.index_name, doc_type=doc_type, id=doc_id, mlt_fields=[field_name], **params)
        except elasticsearch.TransportError as e:
            if not self.silently_fail:
                raise

            self.log.error("Failed to fetch More Like This from Elasticsearch for document '%s': %s", doc_id, e)
            raw_results = {}

        return self._process_results(raw_results, result_class=result_class)

    def _process_results(self, raw_results, highlight=False,
                         result_class=None, distance_point=None,
                         geo_sort=False):
        from haystack import connections
        results = []
        hits = raw_results.get('hits', {}).get('total', 0)
        facets = {}
        spelling_suggestion = None

        if result_class is None:
            result_class = SearchResult

        if self.include_spelling and 'suggest' in raw_results:
            raw_suggest = raw_results['suggest'].get('suggest')
            if raw_suggest:
                spelling_suggestion = ' '.join([word['text'] if len(word['options']) == 0 else word['options'][0]['text'] for word in raw_suggest])

        if 'facets' in raw_results:
            facets = {
                'fields': {},
                'dates': {},
                'queries': {},
            }

            for facet_fieldname, facet_info in raw_results['facets'].items():
                if facet_info.get('_type', 'terms') == 'terms':
                    facets['fields'][facet_fieldname] = [(individual['term'], individual['count']) for individual in facet_info['terms']]
                elif facet_info.get('_type', 'terms') == 'date_histogram':
                    # Elasticsearch provides UTC timestamps with an extra three
                    # decimals of precision, which datetime barfs on.
                    facets['dates'][facet_fieldname] = [(datetime.datetime.utcfromtimestamp(individual['time'] / 1000), individual['count']) for individual in facet_info['entries']]
                elif facet_info.get('_type', 'terms') == 'query':
                    facets['queries'][facet_fieldname] = facet_info['count']

        unified_index = connections[self.connection_alias].get_unified_index()
        indexed_models = unified_index.get_indexed_models()
        content_field = unified_index.document_field

        for raw_result in raw_results.get('hits', {}).get('hits', []):

            result_type         = raw_result['_type']
            app_model_delim_idx = result_type.rfind('_')

            app_label  = result_type[:app_model_delim_idx]
            model_name = result_type[app_model_delim_idx+1:]

            model      = get_model(app_label, model_name)

            if model and model in indexed_models:
                
                index = unified_index.get_index(model)

                # Look for _source, then _fields in case this was a values_list query
                if '_source' in raw_result:
                    source = raw_result['_source']

                elif 'fields' in raw_result:
                    # _source wasn't requested, but we have fields, so this was a 
                    # values_list query. All Elasticsearch's fields results are lists
                    # so we'll need to fix that for anything that isn't multivalued
                    raw_fields = raw_result['fields']
                    for field in raw_fields:
                        # This breaks multi-value fields when they have one value, so gotta
                        # sort out a fix
                        if field in index.fields and index.fields[field].is_multivalued:
                            # leave this as a list
                            continue
                        else:
                            raw_fields[field] = raw_fields[field][0]

                    source = raw_fields
            
                additional_fields = {}
                for key, value in source.items():
                    string_key = str(key)

                    if string_key in index.fields and hasattr(index.fields[string_key], 'convert'):
                        additional_fields[string_key] = index.fields[string_key].convert(value)
                    else:
                        additional_fields[string_key] = self._to_python(value)

                if DJANGO_CT in additional_fields:
                    del(additional_fields[DJANGO_CT])

                if DJANGO_ID in additional_fields:
                    del(additional_fields[DJANGO_ID])

                if 'highlight' in raw_result:
                    additional_fields['highlighted'] = raw_result['highlight'].get(content_field, '')

                if distance_point:
                    additional_fields['_point_of_origin'] = distance_point

                    if geo_sort and raw_result.get('sort'):
                        from haystack.utils.geo import Distance
                        additional_fields['_distance'] = Distance(km=float(raw_result['sort'][0]))
                    else:
                        additional_fields['_distance'] = None

                result = result_class(app_label, model_name, source[DJANGO_ID], raw_result['_score'], **additional_fields)
                results.append(result)
            else:
                hits -= 1

        return {
            'results': results,
            'hits': hits,
            'facets': facets,
            'spelling_suggestion': spelling_suggestion,
        }

    def build_schema(self, fields):
        content_field_name = ''
        mapping = {
            DJANGO_CT: {'type': 'string', 'index': 'not_analyzed', 'include_in_all': False},
            DJANGO_ID: {'type': 'string', 'index': 'not_analyzed', 'include_in_all': False},
        }

        for field_name, field_class in fields.items():
            field_mapping = FIELD_MAPPINGS.get(field_class.field_type, DEFAULT_FIELD_MAPPING).copy()
            if field_class.boost != 1.0:
                field_mapping['boost'] = field_class.boost

            if field_class.document is True:
                content_field_name = field_class.index_fieldname

            # Do this last to override `text` fields.
            if field_mapping['type'] == 'string':
                if field_class.indexed is False or hasattr(field_class, 'facet_for'):
                    field_mapping['index'] = 'not_analyzed'
                    del field_mapping['analyzer']

            mapping[field_class.index_fieldname] = field_mapping

        return (content_field_name, mapping)

    def _iso_datetime(self, value):
        """
        If value appears to be something datetime-like, return it in ISO format.

        Otherwise, return None.
        """
        if hasattr(value, 'strftime'):
            if hasattr(value, 'hour'):
                return value.isoformat()
            else:
                return '%sT00:00:00' % value.isoformat()

    def _from_python(self, value, for_query=False):
        """
         Converts python data types into values digestable for 
         Documents being sent to ES or literals used in queries.
        """

        iso = self._iso_datetime(value)
        if iso:
            return iso
        elif isinstance(value, six.binary_type):
            # TODO: Be stricter.
            return six.text_type(value, errors='replace')
        elif isinstance(value, bool) and for_query:
            # We only want to turn booleans into strings for building
            # query syntax, not for pushing documents
            return str(value).lower()  # cheap json-ing
        elif isinstance(value, set):
            return list(value)
        return value

    def _to_python(self, value):
        """Convert values from ElasticSearch to native Python values."""
        if isinstance(value, (int, float, complex, list, tuple, bool)):
            return value

        if isinstance(value, six.string_types):
            possible_datetime = DATETIME_REGEX.search(value)

            if possible_datetime:
                date_values = possible_datetime.groupdict()

                for dk, dv in date_values.items():
                    date_values[dk] = int(dv)

                return datetime.datetime(
                    date_values['year'], date_values['month'],
                    date_values['day'], date_values['hour'],
                    date_values['minute'], date_values['second'])

        try:
            # This is slightly gross but it's hard to tell otherwise what the
            # string's original type might have been. Be careful who you trust.
            converted_value = eval(value)

            # Try to handle most built-in types.
            if isinstance(
                    converted_value,
                    (int, list, tuple, set, dict, float, complex)):
                return converted_value
        except Exception:
            # If it fails (SyntaxError or its ilk) or we don't trust it,
            # continue on.
            pass

        return value

# DRL_FIXME: Perhaps move to something where, if none of these
#            match, call a custom method on the form that returns, per-backend,
#            the right type of storage?
DEFAULT_FIELD_MAPPING = {'type': 'string', 'analyzer': 'snowball'}
FIELD_MAPPINGS = {
    'edge_ngram': {'type': 'string', 'index_analyzer': 'edgengram_analyzer', 'search_analyzer': 'standard'},
    'ngram':      {'type': 'string', 'index_analyzer': 'edgengram_analyzer', 'search_analyzer': 'standard'},
    'date':       {'type': 'date'},
    'datetime':   {'type': 'date'},

    'location':   {'type': 'geo_point'},        
    'boolean':    {'type': 'boolean'},
    'float':      {'type': 'float'},
    'long':       {'type': 'long'},
    'integer':    {'type': 'long'},

    'string_ci' : {'type': 'string', 'index_analyzer': 'case_insensitive_phrase', 'search_analyzer': 'case_insensitive_phrase'},
}


# Sucks that this is almost an exact copy of what's in the Solr backend,
# but we can't import due to dependencies.
class ElasticsearchSearchQuery(BaseSearchQuery):
    def matching_all_fragment(self):
        return '*:*'

    def add_spatial(self, lat, lon, sfield, distance, filter='bbox'):
        """Adds spatial query parameters to search query"""
        kwargs = {
            'lat': lat,
            'long': long,
            'sfield': sfield,
            'distance': distance,
        }
        self.spatial_query.update(kwargs)

    def add_order_by_distance(self, lat, long, sfield):
        """Orders the search result by distance from point."""
        kwargs = {
            'lat': lat,
            'long': long,
            'sfield': sfield,
        }
        self.order_by_distance.update(kwargs)

    def build_query_fragment(self, field, filter_type, value):
        from haystack import connections
        query_frag = ''

        if not hasattr(value, 'input_type_name'):
            # Handle when we've got a ``ValuesListQuerySet``...
            if hasattr(value, 'values_list'):
                value = list(value)

            if isinstance(value, six.string_types):
                # It's not an ``InputType``. Assume ``Clean``.
                value = Clean(value)
            else:
                value = PythonData(value)

        # Prepare the query using the InputType.
        prepared_value = value.prepare(self)

        if not isinstance(prepared_value, (set, list, tuple)):
            # Then convert whatever we get back to what elasticsearch wants if needed.
            prepared_value = self.backend._from_python(prepared_value, for_query=True)

        # 'content' is a special reserved word, much like 'pk' in
        # Django's ORM layer. It indicates 'no special field'.
        if field == 'content':
            index_fieldname = ''
        else:
            index_fieldname = u'%s:' % connections[self._using].get_unified_index().get_index_fieldname(field)

        filter_types = {
            'contains': u'%s',
            'startswith': u'%s*',
            'exact': u'%s',
            'gt': u'{%s TO *}',
            'gte': u'[%s TO *]',
            'lt': u'{* TO %s}',
            'lte': u'[* TO %s]',
        }

        if value.post_process is False:
            query_frag = prepared_value
        else:
            if filter_type in ['contains', 'startswith']:
                if value.input_type_name == 'exact':
                    query_frag = prepared_value
                else:
                    # Iterate over terms & incorporate the converted form of each into the query.
                    terms = []

                    if isinstance(prepared_value, six.string_types):
                        for possible_value in prepared_value.split(' '):
                            terms.append(filter_types[filter_type] % self.backend._from_python(possible_value, for_query=True))
                    else:
                        terms.append(filter_types[filter_type] % self.backend._from_python(prepared_value, for_query=True))

                    if len(terms) == 1:
                        query_frag = terms[0]
                    else:
                        query_frag = u"(%s)" % " AND ".join(terms)
            elif filter_type == 'in':
                in_options = []
                if len(prepared_value) >= 500:
                    from elation.util.exception import log_warning
                    log_warning(msg="Found %s values in an ES IN clause" % (len(prepared_value),))
                for possible_value in prepared_value:
                    in_options.append(u'"%s"' % self.backend._from_python(possible_value, for_query=True))

                query_frag = u"(%s)" % " OR ".join(in_options)
            elif filter_type == 'range':
                start = self.backend._from_python(prepared_value[0], for_query=True)
                end = self.backend._from_python(prepared_value[1], for_query=True)
                query_frag = u'["%s" TO "%s"]' % (start, end)
            elif filter_type == 'exact':
                if value.input_type_name == 'exact':
                    query_frag = prepared_value
                else:
                    prepared_value = Exact(prepared_value).prepare(self)
                    query_frag = filter_types[filter_type] % prepared_value
            else:
                if value.input_type_name != 'exact':
                    prepared_value = Exact(prepared_value).prepare(self)

                query_frag = filter_types[filter_type] % prepared_value

        if len(query_frag) and not isinstance(value, Raw):
            if not query_frag.startswith('(') and not query_frag.endswith(')'):
                query_frag = "(%s)" % query_frag

        return u"%s%s" % (index_fieldname, query_frag)

    def build_alt_parser_query(self, parser_name, query_string='', **kwargs):
        if query_string:
            kwargs['v'] = query_string

        kwarg_bits = []

        for key in sorted(kwargs.keys()):
            if isinstance(kwargs[key], six.string_types) and ' ' in kwargs[key]:
                kwarg_bits.append(u"%s='%s'" % (key, kwargs[key]))
            else:
                kwarg_bits.append(u"%s=%s" % (key, kwargs[key]))

        return u"{!%s %s}" % (parser_name, ' '.join(kwarg_bits))

    def build_params(self, spelling_query=None, **kwargs):
        search_kwargs = {
            'start_offset': self.start_offset,
            'result_class': self.result_class
        }
        order_by_list = None

        if self.order_by:
            if order_by_list is None:
                order_by_list = []

            for field in self.order_by:
                direction = 'asc'
                if field.startswith('-'):
                    direction = 'desc'
                    field = field[1:]
                
                order_by_list.append((field, direction))

            search_kwargs['sort_by'] = order_by_list

        if self.date_facets:
            search_kwargs['date_facets'] = self.date_facets

        if self.distance_point:
            search_kwargs['distance_point'] = self.distance_point

        if self.dwithin:
            search_kwargs['dwithin'] = self.dwithin

        if self.end_offset is not None:
            search_kwargs['end_offset'] = self.end_offset

        if self.facets:
            search_kwargs['facets'] = self.facets

        if self.fields:
            search_kwargs['fields'] = self.fields

        if self.highlight:
            search_kwargs['highlight'] = self.highlight

        if self.models:
            search_kwargs['models'] = self.models

        if self.narrow_queries:
            search_kwargs['narrow_queries'] = self.narrow_queries

        if self.query_facets:
            search_kwargs['query_facets'] = self.query_facets

        if self.within:
            search_kwargs['within'] = self.within

        if spelling_query:
            search_kwargs['spelling_query'] = spelling_query

        return search_kwargs

    def run(self, spelling_query=None, **kwargs):
        """Builds and executes the query. Returns a list of search results."""
        final_query = self.build_query()
        search_kwargs = self.build_params(spelling_query, **kwargs)

        if kwargs:
            search_kwargs.update(kwargs)

        results = self.backend.search(final_query, **search_kwargs)
        self._results = results.get('results', [])
        self._hit_count = results.get('hits', 0)
        self._facet_counts = self.post_process_facets(results)
        self._spelling_suggestion = results.get('spelling_suggestion', None)

    def run_mlt(self, **kwargs):
        """Builds and executes the query. Returns a list of search results."""
        if self._more_like_this is False or self._mlt_instance is None:
            raise MoreLikeThisError("No instance was provided to determine 'More Like This' results.")

        additional_query_string = self.build_query()
        search_kwargs = {
            'start_offset': self.start_offset,
            'result_class': self.result_class,
            'models': self.models
        }

        if self.end_offset is not None:
            search_kwargs['end_offset'] = self.end_offset - self.start_offset

        results = self.backend.more_like_this(self._mlt_instance, additional_query_string, **search_kwargs)
        self._results = results.get('results', [])
        self._hit_count = results.get('hits', 0)


class ElasticsearchSearchEngine(BaseEngine):
    backend = ElasticsearchSearchBackend
    query = ElasticsearchSearchQuery
