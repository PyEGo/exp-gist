FROM ubuntu:18.04

LABEL maintainer="otc@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python-dev
RUN apt-get update
RUN apt-get install -y python-pip
# install packages
RUN apt-get update
RUN pip install -U pip
RUN apt-get install -y python-crypto-dbg
RUN apt-get install -y python-protobuf
RUN apt-get install -y python-google-auth
RUN pip install datetime
RUN apt-get install -y python-pycryptodome
RUN apt-get install -y python-crypto
RUN apt-get install -y python-google-apputils

ADD snippet.py snippet.py
CMD python snippet.py
