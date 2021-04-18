FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","zipnish"]
RUN ["pip","install","di-py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","pmagpy-cli"]
RUN ["pip","install","pmagpy"]
RUN ["pip","install","ui"]
RUN ["pip","install","Dialogs"]
CMD ["python","snippet.py"]

