FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install docutils-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyserial==3.5
RUN pip install kivy==2.0.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
