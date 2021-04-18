FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","twitter.common.service-thrift"]
RUN ["pip","install","twitter.common.finagle-thrift"]
RUN ["pip","install","lda"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","git"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["apt-get","install","-y","wget"]
RUN ["pip","install","gensim"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
CMD ["python","snippet.py"]

