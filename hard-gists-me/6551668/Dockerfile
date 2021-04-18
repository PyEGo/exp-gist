FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","ndg-httpsclient"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyOpenSSL"]
RUN ["pip","install","pyasn1"]
RUN ["pip","install","pytz"]
CMD ["python","snippet.py"]

