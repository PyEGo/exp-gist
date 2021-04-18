FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pycrypto"]
RUN ["pip","install","php"]
RUN ["pip","install","phpserialize"]
CMD ["python","snippet.py"]

