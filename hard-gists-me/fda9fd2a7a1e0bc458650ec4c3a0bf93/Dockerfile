FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","pycrypto"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","botocore"]
CMD ["python","snippet.py"]

