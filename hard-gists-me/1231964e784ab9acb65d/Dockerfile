FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","raven"]
RUN ["pip","install","ujson"]
RUN ["pip","install","plac"]
CMD ["python","snippet.py"]

