FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pycrypto"]
RUN ["pip","install","M2Crypto"]
RUN ["pip","install","bplist"]
CMD ["python","snippet.py"]

