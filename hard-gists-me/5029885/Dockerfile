FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","OpsletsEc2"]
RUN ["pip","install","gdctools"]
RUN ["pip","install","config"]
CMD ["python","snippet.py"]

