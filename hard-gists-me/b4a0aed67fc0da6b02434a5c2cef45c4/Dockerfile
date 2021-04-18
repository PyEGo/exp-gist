FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","eventlet"]
RUN ["pip","install","django-storage-swift"]
CMD ["python","snippet.py"]

