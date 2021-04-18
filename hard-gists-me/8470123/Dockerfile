FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","python-memcached"]
RUN ["pip","install","hash_ring"]
CMD ["python","snippet.py"]

