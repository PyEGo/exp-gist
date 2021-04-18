FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","bottle"]
RUN ["pip","install","WSGIProxy2"]
CMD ["python","snippet.py"]

