FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","dj-database-url"]
RUN ["pip","install","newrelic"]
RUN ["pip","install","django-storages-redux"]
RUN ["pip","install","django-storages"]
RUN ["pip","install","stor"]
CMD ["python","snippet.py"]

