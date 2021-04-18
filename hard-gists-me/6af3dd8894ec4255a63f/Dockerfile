FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","curl"]
RUN ["pip","install","prettytable"]
CMD ["python","snippet.py"]

