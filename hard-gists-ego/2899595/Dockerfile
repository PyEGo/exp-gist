FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install bind9utils -y
RUN apt-get install curl -y
RUN apt-get install dbus-x11 -y
RUN apt-get install ffmpeg -y
RUN apt-get install imagemagick -y
RUN apt-get install kmod -y
RUN apt-get install libjpeg-dev -y
RUN apt-get install net-tools -y
RUN apt-get install netbase -y
RUN apt-get install nodejs -y
RUN apt-get install psmisc -y
RUN apt-get install software-properties-common -y
RUN apt-get install sudo -y
RUN apt-get install tcpdump -y
RUN apt-get install traceroute -y
RUN apt-get install wget -y
RUN apt-get install xvfb -y
RUN apt-get install zlib1g-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install ajaxuploader==0.3.8
RUN pip install boto==2.49.0
RUN pip install django==3.1.4
RUN pip install eventlet==0.30.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
