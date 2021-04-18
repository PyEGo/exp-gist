FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","conf"]
RUN ["pip","install","celery"]
CMD ["python","snippet.py"]

