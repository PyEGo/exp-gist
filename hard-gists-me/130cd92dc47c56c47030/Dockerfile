FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyd"]
RUN ["pip","install","pydub"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

