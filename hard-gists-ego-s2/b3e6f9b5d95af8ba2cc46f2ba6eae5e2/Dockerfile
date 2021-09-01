FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tk-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install zymtest2==0.1.1
RUN pip install django==3.2.2
RUN pip install algoliasearch-django==1.2.5
RUN pip install pytest==6.2.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
