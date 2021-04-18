FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","androidviewclient"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-compressor"]
CMD ["python","snippet.py"]

