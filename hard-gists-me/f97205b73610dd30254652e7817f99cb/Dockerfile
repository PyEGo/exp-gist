FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","pyzmq"]
RUN ["pip","install","ipykernel"]
CMD ["python","snippet.py"]

