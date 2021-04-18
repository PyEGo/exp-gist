FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","db"]
RUN ["pip","install","gobject"]
RUN ["pip","install","dbpy"]
RUN ["pip","install","db.py"]
RUN ["pip","install","lisa"]
RUN ["pip","install","django-experiments"]
RUN ["pip","install","bluezero"]
CMD ["python","snippet.py"]

