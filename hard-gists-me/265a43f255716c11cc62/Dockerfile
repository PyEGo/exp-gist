FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","db"]
RUN ["pip","install","gobject"]
RUN ["pip","install","db.py"]
RUN ["pip","install","dbpy"]
CMD ["python","snippet.py"]

