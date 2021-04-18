FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install twisted==20.3.0
RUN pip install autobahn==19.11.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
