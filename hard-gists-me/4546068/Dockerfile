FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pycrypto"]
RUN ["pip","install","M2Crypto"]
CMD ["python","snippet.py"]

