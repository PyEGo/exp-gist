FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install adafruit-ads1x15==1.0.2
RUN pip install requests==2.25.0
RUN pip install plotly==4.14.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
