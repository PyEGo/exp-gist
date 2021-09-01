FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install docutils-common -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN apt-get install sphinx-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install docutils==0.17.1
RUN pip install sphinx-testing==0.2.0
RUN pip install sphinx==1.7.9
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
