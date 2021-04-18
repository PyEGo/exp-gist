FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","facepy"]
RUN ["pip","install","Django"]
RUN ["pip","install","django_db"]
CMD ["python","snippet.py"]

