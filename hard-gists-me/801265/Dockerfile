FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","M2Crypto"]
RUN ["pip","install","stomp.py"]
CMD ["python","snippet.py"]

