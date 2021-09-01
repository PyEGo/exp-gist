FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libsodium23 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-river==3.3.0
RUN pip install fab-classic==1.18.1
RUN pip install edx-opaque-keys==2.2.0
RUN pip install fabric==1.14.1
RUN pip install fabric3==1.14.post1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
