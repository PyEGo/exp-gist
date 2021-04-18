FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Django"]
RUN ["pip","install","django-tastypie"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","lxml"]
RUN ["pip","install","django-guardian"]
CMD ["python","snippet.py"]

