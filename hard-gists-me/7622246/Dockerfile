FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","dropbox"]
RUN ["pip","install","be"]
RUN ["pip","install","console"]
RUN ["pip","install","bencode"]
CMD ["python","snippet.py"]

