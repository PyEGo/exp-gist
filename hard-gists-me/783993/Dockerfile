FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","mongo"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","mongoengine"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

