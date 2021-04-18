FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install libblas3 -y
RUN apt-get install libgdal20 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install click==7.1.2
RUN pip install rasterio==1.1.8
RUN pip install fiona==1.8.18
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
