FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","thrift"]
RUN ["pip","install","PyHive"]
CMD ["python","snippet.py"]

