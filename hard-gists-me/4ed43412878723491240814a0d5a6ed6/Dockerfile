FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","khmer"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","scipy"]
CMD ["python","snippet.py"]

