FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","access_points"]
RUN ["pip","install","tensorlayer"]
RUN ["pip","install","futures"]
RUN ["pip","install","data"]
CMD ["python","snippet.py"]

