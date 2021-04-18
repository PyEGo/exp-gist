FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","snippet.py"]

