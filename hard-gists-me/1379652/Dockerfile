FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","ck"]
RUN ["pip","install","Django"]
RUN ["pip","install","requests"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","django-ckeditor"]
CMD ["python","snippet.py"]

