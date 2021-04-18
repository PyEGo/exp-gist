FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","sh"]
RUN ["pip","install","maya"]
RUN ["pip","install","Qt.py"]
RUN ["pip","install","shiboken2"]
CMD ["python","snippet.py"]

