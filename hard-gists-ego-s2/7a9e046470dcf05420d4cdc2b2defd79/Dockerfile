FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install amazon.ion==0.7.0
RUN pip install python-amazon-simple-product-api==2.2.11
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
