FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","CASWSGIMiddleware"]
RUN ["pip","install","django-cas-client"]
CMD ["python","snippet.py"]

