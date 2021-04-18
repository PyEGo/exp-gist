FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","OpsletsEc2"]
RUN ["pip","install","gdctools"]
RUN ["pip","install","Ghost.py"]
RUN ["pip","install","config"]
RUN ["pip","install","ghost"]
CMD ["python","snippet.py"]

