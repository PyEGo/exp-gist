FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install awesome-finder==1.2.3
RUN pip install awesome-aws==0.1.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
