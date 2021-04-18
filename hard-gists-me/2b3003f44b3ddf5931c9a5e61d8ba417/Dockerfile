FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","unicorn"]
RUN ["pip","install","keystone"]
RUN ["pip","install","pwntools"]
RUN ["pip","install","pwn"]
CMD ["python","snippet.py"]

