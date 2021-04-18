FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","twitter.common.service-thrift"]
RUN ["pip","install","twitter.common.finagle-thrift"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
CMD ["python","snippet.py"]

