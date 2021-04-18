FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","db"]
RUN ["pip","install","gobject"]
RUN ["pip","install","dbpy"]
RUN ["pip","install","db.py"]
CMD ["python","snippet.py"]

