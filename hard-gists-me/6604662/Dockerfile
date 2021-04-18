FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","WTForms"]
RUN ["pip","install","WTForms-JSON"]
RUN ["pip","install","SQLAlchemy"]
RUN ["pip","install","wtforms-validators"]
CMD ["python","snippet.py"]

