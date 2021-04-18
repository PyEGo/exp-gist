FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","ZODB3"]
RUN ["pip","install","ZODB"]
CMD ["python","snippet.py"]

