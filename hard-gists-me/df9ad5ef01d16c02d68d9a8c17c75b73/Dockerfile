FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","twitter-text-python"]
RUN ["pip","install","ttp"]
CMD ["python","snippet.py"]

