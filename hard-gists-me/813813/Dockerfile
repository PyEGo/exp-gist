FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","django-munin"]
RUN ["pip","install","Munin"]
CMD ["python","snippet.py"]

