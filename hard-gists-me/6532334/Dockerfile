FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","v4l2"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
CMD ["python","snippet.py"]

