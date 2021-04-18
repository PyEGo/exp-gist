FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","app"]
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
CMD ["python","snippet.py"]

