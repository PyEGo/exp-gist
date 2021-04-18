FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","file-magic"]
RUN ["pip","install","python-magic"]
RUN ["pip","install","python-dateutil"]
CMD ["python","snippet.py"]

