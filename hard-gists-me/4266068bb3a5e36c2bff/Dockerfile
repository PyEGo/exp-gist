FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","epguides-api"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Flask"]
RUN ["pip","install","blockstack"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","django-rest-framework-mongoengine"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

