FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libjs-jquery -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install werkzeug==1.0.1
RUN pip install flask==1.1.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
