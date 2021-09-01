FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install six==1.16.0
RUN pip install elasticsearch==7.12.1
RUN pip install django==3.2.2
RUN pip install django-haystack==3.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
