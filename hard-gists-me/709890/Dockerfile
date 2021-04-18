FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Django"]
RUN ["pip","install","django-tastypie"]
RUN ["pip","install","dj.choices"]
CMD ["python","snippet.py"]

