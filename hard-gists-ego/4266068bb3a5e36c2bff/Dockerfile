FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-rest-framework-mongoengine==3.4.1
RUN pip install django==3.2.2
RUN pip install packt==1.4.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
