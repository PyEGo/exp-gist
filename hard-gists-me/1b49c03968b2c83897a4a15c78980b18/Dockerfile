FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","torch"]
RUN ["pip","install","progress"]
RUN ["pip","install","progressbar"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","pytz"]
RUN ["pip","install","progressbar2"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

