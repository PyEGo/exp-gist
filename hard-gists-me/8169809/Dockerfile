FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","scene"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","console"]
CMD ["python","snippet.py"]

