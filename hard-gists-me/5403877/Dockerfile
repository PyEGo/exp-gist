FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","maya"]
RUN ["pip","install","PySide"]
RUN ["pip","install","Shiboken"]
CMD ["python","snippet.py"]

