FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install fontconfig -y
RUN apt-get install freeglut3 -y
RUN apt-get install libblas3 -y
RUN apt-get install libfreetype6 -y
RUN apt-get install libgl1 -y
RUN apt-get install libglu1-mesa -y
RUN apt-get install libgtk2.0-0 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libopenal1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyglet==1.5.11
RUN pip install wxpython==4.1.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
