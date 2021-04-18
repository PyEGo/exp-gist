FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Flask-SQLAlchemy"]
RUN ["pip","install","Flask-MySQL"]
RUN ["pip","install","celery"]
RUN ["pip","install","myapp"]
CMD ["python","snippet.py"]

