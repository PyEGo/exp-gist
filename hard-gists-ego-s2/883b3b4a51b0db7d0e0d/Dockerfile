FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install docutils-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install sander-daemon==1.0.0
RUN pip install logilab-common==0.63.2
RUN pip install apscheduler==2.1.2
RUN pip install python-daemon==2.3.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
