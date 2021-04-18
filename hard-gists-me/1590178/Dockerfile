FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","WTForms"]
RUN ["pip","install","wtforms-validators"]
RUN ["pip","install","wtforms-widgets"]
CMD ["python","snippet.py"]

