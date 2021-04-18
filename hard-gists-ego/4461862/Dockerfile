FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install build-essential -y
RUN apt-get install curl -y
RUN apt-get install git -y
RUN apt-get install less -y
RUN apt-get install nano -y
RUN apt-get install net-tools -y
RUN apt-get install netcat -y
RUN apt-get install nmap -y
RUN apt-get install openssh-client -y
RUN apt-get install telnet -y
RUN apt-get install vim -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install gitpython==3.1.11
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
