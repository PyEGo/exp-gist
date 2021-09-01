FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libcairo2 -y
RUN apt-get install libdbus-1-3 -y
RUN apt-get install libglib2.0-0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install bluezero==0.6.0
RUN pip install dbus-python==1.2.16
RUN pip install pygobject==3.40.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
