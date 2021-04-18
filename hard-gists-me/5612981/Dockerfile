FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["pip","install","tornado"]
RUN ["pip","install","tornado-redis"]
RUN ["pip","install","tornadoredis"]
CMD ["python","snippet.py"]

