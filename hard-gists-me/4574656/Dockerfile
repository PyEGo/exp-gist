FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-tastypie"]
RUN ["pip","install","django-facebook"]
RUN ["pip","install","django-facebook-connect"]
CMD ["python","snippet.py"]

