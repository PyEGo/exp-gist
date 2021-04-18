FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","scikit-cuda"]
RUN ["pip","install","scikits.audiolab"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

