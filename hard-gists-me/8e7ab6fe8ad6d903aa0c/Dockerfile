FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","syn"]
RUN ["pip","install","synapse"]
RUN ["pip","install","synapseclient"]
CMD ["python","snippet.py"]

