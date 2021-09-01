FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libjs-jquery -y
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install wtforms==2.3.3
RUN pip install pyecore==0.3.0
RUN pip install flask==0.8.1
RUN pip install flask-wtf==0.6
RUN pip install flask-sqlalchemy==0.15
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
