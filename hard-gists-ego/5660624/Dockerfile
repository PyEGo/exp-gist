FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install docutils-common -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN apt-get install sphinx-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install sqlalchemy==1.3.20
RUN pip install pyramid==1.10.5
RUN pip install dogpile.cache==1.1.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
