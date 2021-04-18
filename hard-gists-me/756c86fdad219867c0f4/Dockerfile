FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","image"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","pytz"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","MarkupSafe"]
RUN ["pip","install","Pygments"]
RUN ["pip","install","docutils"]
RUN ["pip","install","Sphinx"]
RUN ["pip","install","snowballstemmer"]
RUN ["pip","install","alabaster"]
RUN ["pip","install","imagesize"]
CMD ["python","snippet.py"]

