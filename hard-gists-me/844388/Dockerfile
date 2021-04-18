FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python"]
RUN ["pip","install","ordereddict"]
RUN ["pip","install","TextTest"]
RUN ["pip","install","PyYAML"]
CMD ["python","snippet.py"]

