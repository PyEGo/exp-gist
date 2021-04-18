FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","17MonIP"]
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Twisted"]
RUN ["pip","install","IPy"]
RUN ["pip","install","beautifulsoup4"]
RUN ["pip","install","ipython"]
CMD ["python","snippet.py"]

