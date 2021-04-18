FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","feedparser"]
RUN ["pip","install","django-contacts"]
RUN ["pip","install","console"]
RUN ["pip","install","Contacts"]
CMD ["python","snippet.py"]

