FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","MySQL-python"]
RUN ["pip","install","mysqlclient"]
RUN ["pip","install","dbutil"]
CMD ["python","snippet.py"]

