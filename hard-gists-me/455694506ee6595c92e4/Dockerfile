FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","chai"]
RUN ["pip","install","BriCA1"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
RUN ["pip","install","chainer"]
CMD ["python","snippet.py"]

