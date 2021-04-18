FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","django-news-page"]
RUN ["pip","install","newspaper"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","snippet.py"]

