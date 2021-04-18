FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install markdown2==2.3.10
RUN pip install uwsgi==2.0.19.1
RUN pip install flask==1.1.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
