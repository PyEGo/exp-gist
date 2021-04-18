FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","di-py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","pmagpy-cli"]
RUN ["pip","install","console"]
RUN ["pip","install","pmagpy"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","Dialogs"]
CMD ["python","snippet.py"]

