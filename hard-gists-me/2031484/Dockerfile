FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Django"]
RUN ["pip","install","django-tastypie"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","mock"]
RUN ["pip","install","raven"]
RUN ["pip","install","pysolr"]
CMD ["python","snippet.py"]

