FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install g++ -y
RUN apt-get install libpq5 -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install psycopg2==2.8.6
RUN pip install twisted==20.3.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
