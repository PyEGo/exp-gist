FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","django-taggit"]
RUN ["pip","install","django-blog-zinnia"]
RUN ["pip","install","Django"]
RUN ["pip","install","django_db"]
CMD ["python","snippet.py"]

