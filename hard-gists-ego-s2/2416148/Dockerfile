FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tornado==6.1
RUN pip install pymongo==2.0.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
