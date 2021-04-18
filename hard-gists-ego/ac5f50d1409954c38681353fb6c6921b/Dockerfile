FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libdbus-1-3 -y
RUN apt-get install libglib2.0-0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install dbus-python==1.2.16
RUN pip install pygobject==2.10.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
