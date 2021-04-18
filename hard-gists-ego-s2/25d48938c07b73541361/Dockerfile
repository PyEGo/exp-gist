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
RUN apt-get install -y python-bs4
RUN apt-get install -y libssl-dev
RUN apt-get install -y python-feedparser
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN pip install livingbio-newspaper
RUN apt-get install -y python-requests
RUN apt-get install -y python3-dev
RUN apt-get install -y g++
RUN pip install gspread

ADD snippet.py snippet.py
CMD python snippet.py
