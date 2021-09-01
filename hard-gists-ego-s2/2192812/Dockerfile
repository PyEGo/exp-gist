FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pygments==2.3.1
RUN pip install httpie==0.8.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
