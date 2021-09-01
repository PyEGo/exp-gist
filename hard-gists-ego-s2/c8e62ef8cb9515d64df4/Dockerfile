FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install ffmpeg -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libgomp1 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libsndfile1 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libtbb2 -y
RUN apt-get install procps -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.20.3
RUN pip install progressbar2==3.53.1
RUN pip install matplotlib==3.4.2
RUN pip install librosa==0.8.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
