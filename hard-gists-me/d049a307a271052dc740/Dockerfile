FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pefile"]
RUN ["pip","install","pycrypto"]
CMD ["python","snippet.py"]

