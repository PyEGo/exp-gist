FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pystache"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

