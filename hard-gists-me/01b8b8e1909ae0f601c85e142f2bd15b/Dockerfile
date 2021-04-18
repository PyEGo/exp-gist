FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","sinaweibopy"]
RUN ["pip","install","weibo"]
RUN ["pip","install","pushbullet.py"]
RUN ["pip","install","xtls"]
CMD ["python","snippet.py"]

