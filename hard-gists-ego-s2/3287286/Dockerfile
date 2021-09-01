FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python python-pip -y
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python-numpy -y
RUN apt-get install python-pandas -y
RUN apt-get install python-rpy2 -y
RUN pip install pandas==0.19.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
