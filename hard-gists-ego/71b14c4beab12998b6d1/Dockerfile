FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install docutils-common -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN apt-get install unzip -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install markdown2==2.3.10
RUN pip install xhtml2pdf==0.2.5
RUN pip install aristotle-metadata-registry==1.5.7
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
