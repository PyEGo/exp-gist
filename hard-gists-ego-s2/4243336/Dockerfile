FROM debian:10
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN cp /usr/bin/python3 /usr/bin/python
RUN cp /usr/bin/pip3 /usr/bin/pip
RUN apt-get update
RUN apt-get install freeglut3 -y
RUN apt-get install libgl1 -y
RUN apt-get install libgl1-mesa-glx -y
RUN apt-get install libglu1-mesa -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python3-pygame -y
RUN apt-get install python3-numpy -y
RUN apt-get install python3-opengl -y
RUN pip install pyopengl==3.1.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
