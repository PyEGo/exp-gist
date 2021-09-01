FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install flask==0.11.1
RUN pip install raven==6.10.0
RUN pip install flask-heroku==0.1.9
RUN pip install flask-sslify==0.1.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
