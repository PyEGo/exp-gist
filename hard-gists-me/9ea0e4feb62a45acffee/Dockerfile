FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","jmb.filters"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","django-filter"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

