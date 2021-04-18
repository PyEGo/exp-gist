FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","Keras"]
RUN ["pip","install","scikit-learn"]
RUN ["pip","install","keras-models"]
RUN ["pip","install","Keras-Preprocessing"]
CMD ["python","snippet.py"]

