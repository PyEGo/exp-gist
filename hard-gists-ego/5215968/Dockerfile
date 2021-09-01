FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pandas==0.13.1
RUN pip install numpy==1.16.6
RUN pip install scipy==1.2.3
RUN pip install matplotlib==2.0.2
RUN pip install qstk==0.2.8
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
