FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","indras_net"]
RUN ["pip","install","Flask"]
RUN ["pip","install","models"]
CMD ["python","snippet.py"]

