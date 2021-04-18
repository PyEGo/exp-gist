FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","docutils"]
RUN ["pip","install","lockfile"]
CMD ["python","snippet.py"]

