FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install lxml==4.6.2
RUN pip install selenium==2.49.2
RUN pip install scrapy==1.3.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
