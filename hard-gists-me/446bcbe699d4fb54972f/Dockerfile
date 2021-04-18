FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","SimpleWebSocketServer"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyOSC"]
CMD ["python","snippet.py"]

