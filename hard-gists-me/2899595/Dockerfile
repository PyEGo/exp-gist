FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","ajax"]
RUN ["pip","install","ajaxuploader"]
RUN ["pip","install","eventlet"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

