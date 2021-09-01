FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install fuse -y
RUN apt-get install libfuse2 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install fuse-python==0.2_pre2
RUN pip install fusepy==3.0.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
