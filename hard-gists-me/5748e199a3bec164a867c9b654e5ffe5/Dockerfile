FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","gym"]
RUN ["pip","install","numpy"]
RUN ["pip","install","Keras"]
RUN ["pip","install","keras-models"]
RUN ["pip","install","gym-wrappers"]
CMD ["python","snippet.py"]

