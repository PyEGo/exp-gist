FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-core"]
RUN ["pip","install","django-test"]
RUN ["pip","install","django-template"]
CMD ["python","snippet.py"]

