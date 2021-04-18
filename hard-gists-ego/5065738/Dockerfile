FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libsodium23 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyyaml==5.3.1
RUN pip install fabric3==1.14.post1
RUN pip install fabric==1.14.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
