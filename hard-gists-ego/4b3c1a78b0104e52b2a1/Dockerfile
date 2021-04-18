FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install docutils-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyjnius==1.3.0.0
RUN pip install kivy==2.0.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
