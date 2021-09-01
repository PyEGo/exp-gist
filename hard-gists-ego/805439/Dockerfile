FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install zope.interface==5.4.0
RUN pip install pyramid==2.0
RUN pip install sqlalchemy==1.4.14
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
