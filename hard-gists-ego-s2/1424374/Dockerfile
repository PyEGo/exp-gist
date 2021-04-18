FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libpcap0.8 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install dpkt==1.9.4
RUN pip install pypcap==1.2.3
RUN pip install ipaddr==2.2.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
