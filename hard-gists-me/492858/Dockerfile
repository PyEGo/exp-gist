FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","thrift"]
RUN ["pip","install","python-memcached"]
RUN ["pip","install","flume"]
RUN ["pip","install","tap.py"]
RUN ["pip","install","tap"]
CMD ["python","snippet.py"]

