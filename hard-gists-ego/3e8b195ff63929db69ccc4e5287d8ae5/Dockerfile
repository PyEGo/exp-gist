FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install xmldiff==0.6.10
RUN pip install numpy==1.19.4
RUN pip install pylint==0.23.0
RUN pip install lasagne==0.1
RUN pip install scipy==1.5.4
RUN pip install theano==1.0.5
RUN pip install dataset==1.4.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
