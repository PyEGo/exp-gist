FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","proj"]
RUN ["pip","install","django-inline-svg"]
RUN ["pip","install","svg.charts"]
RUN ["pip","install","svg.path"]
CMD ["python","snippet.py"]

