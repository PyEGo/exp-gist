FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-storages==1.9.1
RUN pip install django-storages-redux==1.3.3
RUN pip install webvirtmgr==4.8.9
RUN pip install django-storages-azure==1.6.8
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
