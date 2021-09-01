FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install nose==1.3.7
RUN pip install django==3.2.2
RUN pip install mongoengine==0.18.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
