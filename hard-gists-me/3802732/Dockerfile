FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","MySQL-python"]
RUN ["pip","install","xlrd"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","Unidecode"]
RUN ["pip","install","mysqlclient"]
CMD ["python","snippet.py"]

