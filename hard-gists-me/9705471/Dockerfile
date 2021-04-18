FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","RPi.GPIO"]
RUN ["pip","install","bottle"]
CMD ["python","snippet.py"]

