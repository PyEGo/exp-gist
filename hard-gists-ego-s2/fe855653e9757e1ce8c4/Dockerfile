FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install libboost-all-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install procps -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.20.3
RUN pip install lasagne==0.1
RUN pip install scikit-learn==0.24.2
RUN pip install nolearn==0.6.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
