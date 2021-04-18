FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install azure==0.10.2
RUN pip install azure-common==1.1.26
RUN pip install django==3.1.4
RUN pip install edx-opaque-keys==2.1.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
