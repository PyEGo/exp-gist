FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","Keras"]
RUN ["pip","install","keras-models"]
RUN ["pip","install","keras-datasets"]
RUN ["pip","install","keras-utils"]
CMD ["python","snippet.py"]

