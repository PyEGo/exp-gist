FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","CASWSGIMiddleware"]
RUN ["pip","install","django-cas-client"]
RUN ["pip","install","tornado_testing"]
CMD ["python","snippet.py"]

