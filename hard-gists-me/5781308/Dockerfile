FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","six"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","GDAL"]
CMD ["python","snippet.py"]

