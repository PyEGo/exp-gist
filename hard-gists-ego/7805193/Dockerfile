FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install gfortran -y
RUN apt-get install libgeos-dev -y
RUN apt-get install libhdf5-dev -y
RUN apt-get install libopenblas-dev -y
RUN apt-get install openssl -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-polymorphic==3.0.0
RUN pip install django==3.1.4
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
