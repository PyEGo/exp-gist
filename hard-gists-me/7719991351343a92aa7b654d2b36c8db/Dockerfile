FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","robotpy-hal-base"]
RUN ["pip","install","paho-mqtt"]
RUN ["pip","install","HAL"]
CMD ["python","snippet.py"]

