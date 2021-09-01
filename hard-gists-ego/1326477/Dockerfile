FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install flask-sqlalchemy==0.15
RUN pip install flask-script==0.3.3
RUN pip install celery==5.0.4
RUN pip install flask-celery==2.2.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
