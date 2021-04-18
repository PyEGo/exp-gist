FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","dj-database-url"]
RUN ["pip","install","newrelic"]
RUN ["pip","install","django-storages-redux"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","django-storages"]
RUN ["pip","install","boto"]
RUN ["pip","install","stor"]
RUN ["pip","install","boto_utils"]
CMD ["python","snippet.py"]

