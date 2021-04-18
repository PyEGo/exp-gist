FROM ubuntu:18.04

LABEL maintainer="otc@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python-dev
RUN apt-get update
RUN apt-get install -y python-pip
# install packages
RUN apt-get update
RUN apt-get install -y python-googleapi
RUN apt-get install -y python-oauth2client

ADD snippet.py snippet.py
CMD python snippet.py
