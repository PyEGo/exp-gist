FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","plotly"]
RUN ["pip","install","RPi.GPIO"]
RUN ["pip","install","Adafruit-ADS1x15"]
CMD ["python","snippet.py"]

