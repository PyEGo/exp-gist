FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","redispy"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","redis"]
RUN ["apt-get","install","-y","libmemcached-dev"]
RUN ["pip","install","pylibmc"]
CMD ["python","snippet.py"]

