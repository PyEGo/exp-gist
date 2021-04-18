FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","tw2.protovis.core"]
RUN ["pip","install","awesome-aws"]
RUN ["pip","install","tw2.forms"]
RUN ["pip","install","tw2.sqla"]
RUN ["pip","install","tw2.core"]
CMD ["python","snippet.py"]

