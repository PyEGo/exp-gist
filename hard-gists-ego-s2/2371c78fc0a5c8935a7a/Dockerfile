FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install chardet==4.0.0
RUN pip install byteark==0.0.12
RUN pip install python-pptx==0.6.18
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
