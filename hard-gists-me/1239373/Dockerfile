FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","BeautifulSoup"]
CMD ["python","snippet.py"]

