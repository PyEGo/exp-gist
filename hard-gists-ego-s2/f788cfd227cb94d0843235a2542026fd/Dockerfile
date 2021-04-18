FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install cython3 -y
RUN apt-get install docutils-common -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libjs-sphinxdoc -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install procps -y
RUN apt-get install sphinx-common -y
RUN apt-get install sphinx-rtd-theme-common -y
RUN apt-get install tk-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install spacy==2.3.5
RUN pip install allennlp==0.9.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
