FROM python:3.8
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install portpicker==1.3.1
RUN pip install tensorflow==2.4.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
