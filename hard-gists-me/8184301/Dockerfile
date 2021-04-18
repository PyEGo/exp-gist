FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
CMD ["python","snippet.py"]

