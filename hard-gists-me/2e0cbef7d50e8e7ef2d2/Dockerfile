FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","youtube-python"]
RUN ["pip","install","pip"]
RUN ["pip","install","youtube_dl"]
CMD ["python","snippet.py"]

