FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","future"]
RUN ["pip","install","six"]
RUN ["pip","install","PasteDeploy"]
RUN ["pip","install","PasteScript"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","WebOb"]
RUN ["pip","install","Paste"]
CMD ["python","snippet.py"]

