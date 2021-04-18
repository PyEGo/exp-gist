FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","gobject"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","PyGTK"]
CMD ["python","snippet.py"]

