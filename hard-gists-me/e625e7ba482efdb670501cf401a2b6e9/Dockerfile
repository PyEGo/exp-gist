FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","snippet.py"]

