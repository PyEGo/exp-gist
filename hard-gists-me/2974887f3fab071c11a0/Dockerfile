FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","em-keyboard"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","PyVirtualDisplay"]
RUN ["pip","install","selenium"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

