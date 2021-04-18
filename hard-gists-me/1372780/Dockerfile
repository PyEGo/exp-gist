FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simpl"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","simplejson"]
RUN ["pip","install","pymongo"]
RUN ["pip","install","pymongo_dbref"]
CMD ["python","snippet.py"]

