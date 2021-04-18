FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dpkt"]
RUN ["pip","install","NetfilterQueue"]
CMD ["python","snippet.py"]

