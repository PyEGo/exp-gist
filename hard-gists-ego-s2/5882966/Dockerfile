FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ieee-data -y
RUN apt-get install libpcap0.8 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pcapy==0.11.4
RUN pip install netifaces==0.10.9
RUN pip install netaddr==0.8.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
