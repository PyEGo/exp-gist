FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install busybox -y
RUN apt-get install fonts-ipaexfont -y
RUN apt-get install libglib2.0-0 -y
RUN apt-get install libsm6 -y
RUN apt-get install libxext6 -y
RUN apt-get install libxrender1 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django==1.11.29
RUN pip install cherrypy==17.2.0.post0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
