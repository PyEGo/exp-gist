FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","gs.dmarc"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","Flask"]
RUN ["pip","install","gspread"]
RUN ["pip","install","gspreed"]
RUN ["pip","install","feedparser"]
RUN ["pip","install","django-news-page"]
RUN ["pip","install","newspaper"]
CMD ["python","snippet.py"]

