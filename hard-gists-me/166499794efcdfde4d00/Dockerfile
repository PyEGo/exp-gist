FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","clip.py"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","clipboard"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

