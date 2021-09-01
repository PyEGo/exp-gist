FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libxml2-dev -y
RUN apt-get install net-tools -y
RUN apt-get install nmap -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install python-mpd2==3.0.4
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
