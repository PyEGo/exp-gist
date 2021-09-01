FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libqpdf21 -y
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install beautifulsoup4==4.9.3
RUN pip install img2pdf==0.4.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
