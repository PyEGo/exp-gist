FROM python:3.8
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install docutils-common -y
RUN apt-get install graphviz -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libcdt5 -y
RUN apt-get install libcgraph6 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tk-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.19.4
RUN pip install syntaxnet-with-tensorflow==0.2
RUN pip install tensorflow==2.4.0
RUN pip install gensim==3.8.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
