FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","couchbase"]
RUN ["pip","install","Flask-Sessions"]
CMD ["python","snippet.py"]

