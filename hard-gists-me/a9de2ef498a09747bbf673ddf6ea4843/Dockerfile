FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","tqdm"]
RUN ["pip","install","Edward"]
RUN ["pip","install","tensorflow"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

