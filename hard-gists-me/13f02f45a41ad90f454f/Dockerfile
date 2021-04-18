FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","clip.py"]
RUN ["pip","install","keychain"]
RUN ["pip","install","clipboard"]
RUN ["pip","install","console"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

