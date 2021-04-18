FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","nltk"]
RUN ["pip","install","pygraph-cli"]
CMD ["python","snippet.py"]

