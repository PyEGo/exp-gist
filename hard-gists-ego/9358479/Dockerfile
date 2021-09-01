FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install git -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tk-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install python-statsd==1.6.4
RUN pip install django-pipeline==1.2.24
RUN pip install flask==0.11.1
RUN pip install sqlalchemy==1.4.14
RUN pip install pytest==6.2.1
RUN pip install google-cloud-storage==1.0.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
