FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","torch"]
RUN ["pip","install","torchvision"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

