FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install plac==1.3.3
RUN pip install ujson==4.0.1
RUN pip install spacy==1.6.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
