FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","capstone"]
CMD ["python","snippet.py"]

