FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","mock"]
RUN ["pip","install","PyHamcrest"]
CMD ["python","snippet.py"]

