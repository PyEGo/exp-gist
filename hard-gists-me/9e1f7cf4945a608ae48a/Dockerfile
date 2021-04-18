FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pyd"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pydbg"]
CMD ["python","snippet.py"]

