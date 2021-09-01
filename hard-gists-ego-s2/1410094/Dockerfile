FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install procps -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install nltk==3.6.2
RUN pip install matplotlib==3.4.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
