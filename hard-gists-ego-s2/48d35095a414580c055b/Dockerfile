FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install urllib3==1.26.2
RUN pip install scikit-image==0.14.5
RUN pip install pandas==0.22.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
