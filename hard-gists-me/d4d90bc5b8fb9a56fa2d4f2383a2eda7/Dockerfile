FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","unicorn"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","capstone"]
RUN ["pip","install","keystone"]
CMD ["python","snippet.py"]

