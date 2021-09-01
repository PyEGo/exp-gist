FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install flask==0.11.1
RUN pip install gunicorn==20.1.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
