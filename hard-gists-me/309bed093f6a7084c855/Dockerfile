FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","selena"]
RUN ["pip","install","predikto-elasticsearch"]
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","elasticsearch"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","pandas"]
CMD ["python","snippet.py"]

