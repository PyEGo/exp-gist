FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","simpl"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","celery"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-celery"]
RUN ["pip","install","simplejson"]
CMD ["python","snippet.py"]

