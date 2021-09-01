FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install bind9utils -y
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install dbus-x11 -y
RUN apt-get install ffmpeg -y
RUN apt-get install g++ -y
RUN apt-get install ieee-data -y
RUN apt-get install imagemagick -y
RUN apt-get install kmod -y
RUN apt-get install libjpeg-dev -y
RUN apt-get install libmagic1 -y
RUN apt-get install libssl-dev -y
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
RUN pip install eventlet==0.31.0
RUN pip install django-storage-swift==1.2.19
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
