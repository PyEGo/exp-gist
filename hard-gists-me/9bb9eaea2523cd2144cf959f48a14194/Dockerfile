FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","requests"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-cors-headers"]
RUN ["pip","install","djangorestframework-jwt"]
CMD ["python","snippet.py"]

