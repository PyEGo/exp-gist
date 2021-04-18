FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","pandas"]
RUN ["apt-get","install","-y","r-base"]
RUN ["pip","install","rpy2"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

