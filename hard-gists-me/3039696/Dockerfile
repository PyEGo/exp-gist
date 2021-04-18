FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","js.tinymce"]
RUN ["pip","install","js.bootstrap"]
RUN ["pip","install","js.fullcalendar"]
RUN ["pip","install","Django"]
RUN ["pip","install","South"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","djangorestframework"]
RUN ["pip","install","jsonfield"]
RUN ["pip","install","django_db"]
CMD ["python","snippet.py"]

