FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","xlrd"]
RUN ["pip","install","python-pptx"]
RUN ["pip","install","reportlab"]
RUN ["pip","install","PyPDF2"]
CMD ["python","snippet.py"]

