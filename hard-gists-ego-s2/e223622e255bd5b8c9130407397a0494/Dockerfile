FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ffmpeg -y
RUN apt-get install gfortran -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libedit-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libgomp1 -y
RUN apt-get install libhdf5-dev -y
RUN apt-get install liblapack-dev -y
RUN apt-get install liblapack3 -y
RUN apt-get install libopenblas-dev -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libsndfile1 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libtbb2 -y
RUN apt-get install pkg-config -y
RUN apt-get install procps -y
RUN apt-get install wget -y
RUN apt-get install zlib1g-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install scipy==1.2.3
RUN pip install matplotlib==2.1.2
RUN pip install matplotlib-venn==0.2
RUN pip install librosa==0.7.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
