FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install libffi-dev -y
RUN apt-get install libjs-jquery -y
RUN apt-get install libjs-mathjax -y
RUN apt-get install libjs-requirejs -y
RUN apt-get install libssl-dev -y
RUN apt-get install libyaml-dev -y
RUN apt-get install libzmq5 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install nbconvert==6.0.7
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
