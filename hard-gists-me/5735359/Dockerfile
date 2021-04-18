FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","scikit-image"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

