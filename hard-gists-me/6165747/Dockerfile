FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","lightning-python"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
RUN ["pip","install","numba"]
RUN ["pip","install","scipy"]
CMD ["python","snippet.py"]

