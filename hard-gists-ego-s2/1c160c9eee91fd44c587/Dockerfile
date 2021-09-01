FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install scikit-image==0.14.5
RUN pip install moviepy==1.0.3
RUN pip install moviepy-patch==1.0.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
