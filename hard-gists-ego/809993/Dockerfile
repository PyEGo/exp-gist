FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-oscar-paypal==0.1.1
RUN pip install django-storages==1.0
RUN pip install django==1.11.29
RUN pip install django-tastypie==0.14.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
