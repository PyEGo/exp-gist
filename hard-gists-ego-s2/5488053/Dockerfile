FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libfreetype6-dev -y
RUN apt-get install libxml2-dev -y
RUN apt-get install make -y
RUN apt-get install wget -y
RUN apt-get install zlib1g-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install freetype-py==2.2.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
