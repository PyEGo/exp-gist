FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","MySQL-python"]
RUN ["pip","install","mysqlclient"]
RUN ["pip","install","ltchinese"]
RUN ["pip","install","wordnik"]
CMD ["python","snippet.py"]

