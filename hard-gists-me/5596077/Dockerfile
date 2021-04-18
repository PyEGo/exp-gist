FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","six"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","python-gflags"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

