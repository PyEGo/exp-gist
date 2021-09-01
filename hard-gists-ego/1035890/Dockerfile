FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install gfortran -y
RUN apt-get install git -y
RUN apt-get install libatlas-base-dev -y
RUN apt-get install libsodium23 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install simplejson==3.17.2
RUN pip install dpxdt==0.1.5
RUN pip install fabric3==1.14.post1
RUN pip install fabric==1.14.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
