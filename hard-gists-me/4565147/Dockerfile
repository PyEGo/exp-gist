FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","future"]
RUN ["pip","install","tornado"]
RUN ["pip","install","iptools"]
CMD ["python","snippet.py"]

