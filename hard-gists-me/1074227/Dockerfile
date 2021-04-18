FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dnspython"]
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","dnslib"]
RUN ["pip","install","gevent"]
CMD ["python","snippet.py"]

