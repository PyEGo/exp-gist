FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install busybox -y
RUN apt-get install docutils-common -y
RUN apt-get install fonts-ipaexfont -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libglib2.0-0 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsm6 -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install libxext6 -y
RUN apt-get install libxrender1 -y
RUN apt-get install tk-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install gensim==3.8.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
