FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install dash-html-components==1.1.1
RUN pip install dash-core-components==1.16.0
RUN pip install pandas-datareader==0.9.0
RUN pip install dash==1.20.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
