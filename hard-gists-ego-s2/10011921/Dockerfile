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
RUN apt-get install -y python-protobuf
RUN pip install webapp2
RUN apt-get install -y python-google-auth
RUN apt-get install -y python-oauth2client
RUN apt-get install -y python-jinja2
RUN apt-get install -y python-googleapi
RUN apt-get install -y python-google-apputils
RUN apt-get install -y python-httplib2

ADD snippet.py snippet.py
CMD python snippet.py
