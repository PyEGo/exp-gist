FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pytz==2021.1
RUN pip install pexpect==4.8.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
