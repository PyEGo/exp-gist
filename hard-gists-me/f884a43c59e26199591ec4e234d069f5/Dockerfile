FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","iquery"]
RUN ["pip","install","tickets"]
RUN ["pip","install","runtime"]
CMD ["python","snippet.py"]

