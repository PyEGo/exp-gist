FROM debian:10
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install python python-pip -y
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python-rospy -y
RUN pip install ws4py==0.5.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
