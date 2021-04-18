FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","onespacemedia-cms"]
RUN ["pip","install","Django"]
RUN ["pip","install","psycopg2"]
RUN ["apt-get","install","-y","postgresql-client"]
RUN ["pip","install","django-modeltranslation"]
RUN ["pip","install","easy-thumbnails"]
RUN ["pip","install","django-cms"]
RUN ["pip","install","django_db"]
CMD ["python","snippet.py"]

