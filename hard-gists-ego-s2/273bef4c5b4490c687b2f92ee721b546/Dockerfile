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
RUN apt-get install -y python-numpy-dbg
RUN apt-get install -y python-opencv
RUN apt-get install -y python-numpy
RUN pip install mxnet-cu90mkl

ADD snippet.py snippet.py
CMD python snippet.py
