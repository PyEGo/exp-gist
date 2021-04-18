FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pycrypto"]
RUN ["pip","install","bcrypt"]
CMD ["python","snippet.py"]

