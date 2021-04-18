FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","secret"]
RUN ["pip","install","carto"]
RUN ["pip","install","django-cart"]
RUN ["pip","install","cartodb"]
CMD ["python","snippet.py"]

