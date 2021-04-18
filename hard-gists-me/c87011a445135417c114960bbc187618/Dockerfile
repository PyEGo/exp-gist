FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","di-py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","Keras"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyspark"]
RUN ["pip","install","distkeras"]
CMD ["python","snippet.py"]

