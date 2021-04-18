FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","Django"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","django-appconf"]
RUN ["pip","install","django-classy-tags"]
CMD ["python","snippet.py"]

