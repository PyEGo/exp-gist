FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","mongo"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","Django"]
RUN ["pip","install","mongoengine"]
RUN ["pip","install","django-test"]
RUN ["pip","install","pymongo"]
CMD ["python","snippet.py"]

