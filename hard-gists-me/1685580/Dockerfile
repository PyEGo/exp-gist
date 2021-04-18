FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Flask-SQLAlchemy"]
RUN ["pip","install","Flask-MySQL"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","pyodbc"]
CMD ["python","snippet.py"]

