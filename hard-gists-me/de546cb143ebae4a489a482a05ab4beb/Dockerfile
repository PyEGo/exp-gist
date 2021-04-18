FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","notmuch"]
RUN ["pip","install","em-keyboard"]
CMD ["python","snippet.py"]

