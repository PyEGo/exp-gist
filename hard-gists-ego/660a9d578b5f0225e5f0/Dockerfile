FROM python:2.7-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pillow==6.0.0
RUN pip install numpy==1.16.6
RUN pip install scipy==1.2.3
RUN pip install grakn-client==1.8.1
RUN pip install google-cloud-storage==1.29.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
