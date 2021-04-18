FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","bson"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","androidviewclient"]
RUN ["pip","install","Django"]
RUN ["pip","install","pymongo"]
CMD ["python","snippet.py"]

