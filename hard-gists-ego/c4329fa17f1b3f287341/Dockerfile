FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install thrift==0.13.0
RUN pip install pyhive==0.6.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
