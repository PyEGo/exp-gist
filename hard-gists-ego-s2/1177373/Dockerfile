FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install redis==3.5.3
RUN pip install scrapy==1.3.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
