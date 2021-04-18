FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","python-nomad"]
RUN ["pip","install","nomad"]
CMD ["python","snippet.py"]

