FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libjs-jquery -y
RUN apt-get install libjs-underscore -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install simplejson==3.17.2
RUN pip install couchdb==1.2
RUN pip install flask==1.1.2
RUN pip install flask-sqlalchemy==0.15
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
