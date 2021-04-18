FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","phue"]
RUN ["pip","install","RPi.GPIO"]
CMD ["python","snippet.py"]

