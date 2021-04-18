FROM python:3.8
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install apache-airflow-backport-providers-elasticsearch==2020.11.13
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
