FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","django-push-notifications"]
RUN ["pip","install","django-push-notifications-goinnn"]
CMD ["python","snippet.py"]

