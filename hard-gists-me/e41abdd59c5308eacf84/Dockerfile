FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","maya"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","mayavi"]
CMD ["python","snippet.py"]

