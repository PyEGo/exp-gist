FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install libjs-jquery -y
RUN apt-get install liblapack3 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install visvis==1.13.0
RUN pip install pymongo==3.11.2
RUN pip install flask==1.1.2
RUN pip install mdanalysis==0.10.0
RUN pip install dbt-helper==0.5.0
RUN pip install spotdl==0.9.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
