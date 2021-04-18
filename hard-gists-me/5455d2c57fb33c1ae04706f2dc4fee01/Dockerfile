FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","chaco"]
RUN ["pip","install","baz"]
RUN ["pip","install","Mypackage"]
CMD ["python","snippet.py"]

