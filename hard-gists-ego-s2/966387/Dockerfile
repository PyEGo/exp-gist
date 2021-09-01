FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python python-pip -y
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python-django -y
RUN apt-get install python-twitter -y
RUN apt-get install python-cjson-dbg -y
RUN apt-get install python-cjson -y
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
