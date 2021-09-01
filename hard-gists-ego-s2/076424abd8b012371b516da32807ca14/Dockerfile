FROM python:3.9
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pandas==1.2.4
RUN pip install apache-airflow-backport-providers-segment==2021.3.17
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
