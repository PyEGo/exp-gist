FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","seria"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","virtualenv"]
RUN ["pip","install","pyserial"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","serial"]
CMD ["python","snippet.py"]

