FROM ubuntu:18.04

LABEL maintainer="otc@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python-dev
RUN apt-get update
RUN apt-get install -y python-pip
# install packages
RUN apt-get update
RUN apt-get install -y python-caldav
RUN apt-get install -y python-fedora
RUN apt-get install -y python-mapbox-vector-tile
RUN apt-get install -y python-circuits
RUN apt-get install -y python-pbcommand
RUN apt-get install -y python-biom-format
RUN apt-get install -y python-sqlalchemy-ext
RUN apt-get install -y python-stetl
RUN apt-get install -y python-phply
RUN apt-get install -y python-overpy
RUN apt-get install -y python-proxmoxer
RUN apt-get install -y python-django-prometheus
RUN apt-get install -y python-forge
RUN apt-get install -y python-remotecv
RUN apt-get install -y python-ghost
RUN apt-get install -y python-poster
RUN apt-get install -y python-softlayer
RUN apt-get install -y python-libturpial
RUN apt-get install -y python-turbogears2
RUN apt-get install -y python-pytest
RUN apt-get install -y python-flask
RUN apt-get install -y python-sqlalchemy
RUN apt-get install -y python-chargebee

ADD snippet.py snippet.py
CMD python snippet.py
