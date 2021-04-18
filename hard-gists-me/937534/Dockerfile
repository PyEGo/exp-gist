FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","pandas"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","nibabel"]
RUN ["pip","install","scipy"]
CMD ["python","snippet.py"]

