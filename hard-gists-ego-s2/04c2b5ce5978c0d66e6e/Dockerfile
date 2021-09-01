FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install remi==2021.3.2
RUN pip install python-editor==1.0.4
RUN pip install django-categories==0.6
RUN pip install webvirtmgr==4.8.9
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
