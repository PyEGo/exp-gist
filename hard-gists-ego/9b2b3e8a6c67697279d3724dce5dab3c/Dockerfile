FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install dash-html-components==1.1.1
RUN pip install dash-core-components==1.16.0
RUN pip install pandas==1.2.4
RUN pip install plotly==4.14.1
RUN pip install dash==1.20.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
