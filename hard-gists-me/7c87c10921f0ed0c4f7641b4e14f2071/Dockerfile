FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","gdctools"]
RUN ["pip","install","OpsletsEc2"]
RUN ["pip","install","config"]
RUN ["pip","install","tensorflow"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

