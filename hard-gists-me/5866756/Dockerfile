FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","docutils"]
RUN ["pip","install","pydocumentdb"]
RUN ["pip","install","Sphinx"]
CMD ["python","snippet.py"]

