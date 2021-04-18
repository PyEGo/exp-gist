FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","django-cache-machine"]
RUN ["pip","install","requests"]
RUN ["pip","install","pyramid"]
RUN ["pip","install","pip"]
RUN ["pip","install","gunicorn"]
RUN ["pip","install","dogpile.cache"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","snippet.py"]

