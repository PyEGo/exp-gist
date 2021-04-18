FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install httplib2==0.18.1
RUN pip install docopt==0.6.2
RUN pip install google-api-python-client==1.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
