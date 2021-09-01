FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libjs-jquery -y
RUN apt-get install libmemcached11 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pylibmc==1.6.1
RUN pip install werkzeug==0.16.1
RUN pip install flask==0.11.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
