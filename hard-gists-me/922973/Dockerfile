FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","six"]
RUN ["apt-get","install","-y","libssl-dev"]
RUN ["apt-get","install","-y","libffi-dev"]
RUN ["pip","install","PyYAML"]
RUN ["pip","install","redis"]
RUN ["pip","install","click"]
RUN ["apt-get","install","-y","vim"]
RUN ["pip","install","fakeredis"]
RUN ["pip","install","riak"]
CMD ["python","snippet.py"]

