FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-river==3.3.0
RUN pip install edx-opaque-keys==2.2.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
