FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas"]
RUN ["pip","install","scikit-image"]
RUN ["pip","install","numpy"]
RUN ["pip","install","skimage"]
CMD ["python","snippet.py"]

