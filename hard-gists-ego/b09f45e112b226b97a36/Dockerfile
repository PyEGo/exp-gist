FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install jinja2==2.11.2
RUN pip install pyyaml==5.3.1
RUN pip install markdown==3.3.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
