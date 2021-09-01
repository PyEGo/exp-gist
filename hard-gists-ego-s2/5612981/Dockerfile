FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tornado==6.1
RUN pip install redis==3.5.3
RUN pip install redis-py-with-geo==2.10.5
RUN pip install tornado-redis==2.4.18
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
