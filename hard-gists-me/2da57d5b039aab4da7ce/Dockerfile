FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dpkt"]
RUN ["apt-get","install","-y","wget"]
RUN ["apt-get","install","-y","python"]
RUN ["apt-get","install","-y","libpcap-dev"]
RUN ["pip","install","pcapy"]
RUN ["pip","install","be"]
RUN ["pip","install","bencode"]
CMD ["python","snippet.py"]

