FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","ccy"]
RUN ["pip","install","cffi"]
RUN ["pip","install","Cython"]
CMD ["python","snippet.py"]

