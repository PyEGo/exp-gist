FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","collectd"]
RUN ["pip","install","Murmur"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Django"]
RUN ["pip","install","gunicorn"]
RUN ["pip","install","parse-type"]
RUN ["pip","install","behave"]
RUN ["pip","install","parse"]
RUN ["pip","install","ice"]
CMD ["python","snippet.py"]

