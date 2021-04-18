FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pdfminer"]
RUN ["pip","install","pdfminer.six"]
CMD ["python","snippet.py"]

