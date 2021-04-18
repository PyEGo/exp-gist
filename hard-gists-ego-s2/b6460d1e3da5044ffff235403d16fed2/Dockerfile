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
RUN apt-get install -y python-scipy-dbg
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y python3-dev
RUN apt-get install -y python-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y python-pip
RUN apt-get install -y python-numpy-dbg
RUN apt-get install -y python-ipython
RUN apt-get install -y python3
RUN apt-get install -y wget
RUN apt-get install -y python-scipy
RUN apt-get install -y git
RUN apt-get install -y python-numpy
RUN apt-get install -y g++
RUN apt-get install -y gfortran
RUN pip install utils
RUN pip install packt

ADD snippet.py snippet.py
CMD python snippet.py
