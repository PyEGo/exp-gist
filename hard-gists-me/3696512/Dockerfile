FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pdfminer.six"]
RUN ["pip","install","pdfminer"]
CMD ["python","snippet.py"]

