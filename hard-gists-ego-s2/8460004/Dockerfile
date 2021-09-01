FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install redis==3.5.3
RUN pip install redis-py-with-geo==2.10.5
RUN pip install kombu==5.0.2
RUN pip install celery==5.0.4
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
