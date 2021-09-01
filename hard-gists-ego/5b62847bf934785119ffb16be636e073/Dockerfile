FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install html2text==2017.10.4
RUN pip install webvirtmgr==4.8.9
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
