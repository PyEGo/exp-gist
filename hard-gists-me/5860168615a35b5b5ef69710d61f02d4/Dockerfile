FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","mysql-connector"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","SQLAlchemy"]
CMD ["python","snippet.py"]

