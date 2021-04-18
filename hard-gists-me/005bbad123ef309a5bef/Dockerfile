FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","python-memcached"]
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["pip","install","memcache"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","snippet.py"]

