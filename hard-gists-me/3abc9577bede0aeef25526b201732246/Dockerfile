FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","idc"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","yara-python"]
RUN ["pip","install","yara"]
CMD ["python","snippet.py"]

