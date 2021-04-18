FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","wget"]
RUN ["pip","install","oslo.utils"]
RUN ["pip","install","python-glanceclient"]
RUN ["pip","install","python-keystoneclient"]
CMD ["python","snippet.py"]

