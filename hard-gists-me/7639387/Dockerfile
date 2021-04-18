FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","python-constraint"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","sympy"]
RUN ["pip","install","networkx"]
RUN ["pip","install","glpk"]
RUN ["pip","install","constraint"]
CMD ["python","snippet.py"]

