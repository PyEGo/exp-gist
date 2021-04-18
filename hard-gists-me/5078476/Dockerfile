FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","MySQL-python"]
RUN ["pip","install","unicodecsv"]
RUN ["pip","install","mysqlclient"]
CMD ["python","snippet.py"]

