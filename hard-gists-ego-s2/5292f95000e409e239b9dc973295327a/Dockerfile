FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tk-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install zymtest2==0.1.1
RUN pip install numpy==1.20.3
RUN pip install keras==2.4.3
RUN pip install pytest==6.2.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
