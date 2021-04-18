FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","watson-auth"]
RUN ["pip","install","django-watson"]
RUN ["pip","install","watson-db"]
RUN ["pip","install","watson-common"]
RUN ["pip","install","watson-framework"]
RUN ["pip","install","Watson"]
CMD ["python","snippet.py"]

