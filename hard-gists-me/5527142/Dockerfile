FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","stream-python"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","astropy"]
CMD ["python","snippet.py"]

