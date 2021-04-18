FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pdfminer.six"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pdfminer"]
RUN ["pip","install","pyPdf"]
CMD ["python","snippet.py"]

