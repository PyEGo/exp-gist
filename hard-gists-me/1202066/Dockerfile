FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","redispy"]
RUN ["pip","install","WebCore"]
RUN ["pip","install","redis"]
CMD ["python","snippet.py"]

