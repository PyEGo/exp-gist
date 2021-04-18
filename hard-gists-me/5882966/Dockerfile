FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","wget"]
RUN ["apt-get","install","-y","python"]
RUN ["apt-get","install","-y","libpcap-dev"]
RUN ["pip","install","pcapy"]
RUN ["pip","install","netifaces"]
RUN ["pip","install","netaddr"]
CMD ["python","snippet.py"]

