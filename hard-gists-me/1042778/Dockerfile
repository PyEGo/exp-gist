FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","python-cjson"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","raven"]
RUN ["pip","install","ujson"]
RUN ["pip","install","simplejson"]
CMD ["python","snippet.py"]

