FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","wget"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","python-keystoneclient"]
RUN ["pip","install","oslo.utils"]
RUN ["pip","install","python-glanceclient"]
RUN ["pip","install","python-cinderclient"]
RUN ["pip","install","python-neutronclient"]
RUN ["pip","install","python-novaclient"]
CMD ["python","snippet.py"]

