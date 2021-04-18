FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","MySQL-python"]
RUN ["pip","install","mysqlclient"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","matplotlib"]
CMD ["python","snippet.py"]

