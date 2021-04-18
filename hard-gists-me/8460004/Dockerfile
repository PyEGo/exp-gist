FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["pip","install","celery"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","amqp"]
RUN ["pip","install","kombu"]
RUN ["pip","install","redis-sentinel"]
CMD ["python","snippet.py"]

