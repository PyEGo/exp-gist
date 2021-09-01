FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tap.py==3.0
RUN pip install thrift==0.13.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
