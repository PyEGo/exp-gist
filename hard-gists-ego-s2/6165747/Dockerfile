FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install busybox -y
RUN apt-get install ca-certificates -y
RUN apt-get install fonts-ipaexfont -y
RUN apt-get install g++ -y
RUN apt-get install gfortran -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libedit-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libglib2.0-0 -y
RUN apt-get install libgomp1 -y
RUN apt-get install libhdf5-dev -y
RUN apt-get install liblapack-dev -y
RUN apt-get install liblapack3 -y
RUN apt-get install libopenblas-dev -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsm6 -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install libtbb2 -y
RUN apt-get install libxext6 -y
RUN apt-get install libxrender1 -y
RUN apt-get install pkg-config -y
RUN apt-get install tk-dev -y
RUN apt-get install wget -y
RUN apt-get install zlib1g-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install pylightning==0.0.7.3
RUN pip install scipy==1.2.3
RUN pip install numba==0.44.1
RUN pip install scikit-learn==0.20.4
RUN pip install lightning-python==1.2.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
