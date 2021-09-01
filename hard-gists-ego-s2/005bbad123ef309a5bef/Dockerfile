FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install redis==3.5.3
RUN pip install redis-py-with-geo==2.10.5
RUN pip install python-memcached==1.59
RUN pip install requests==2.25.0
RUN pip install sqlalchemy==1.4.14
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
