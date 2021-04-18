FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install graphviz -y
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libjs-sphinxdoc -y
RUN apt-get install liblapack3 -y
RUN apt-get install libpq5 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN apt-get install procps -y
RUN apt-get install qt4-designer -y
RUN apt-get install sphinx-rtd-theme-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install psycopg2==2.5.5
RUN pip install pulsar==0.2.1
RUN pip install lmfit==0.6
RUN pip install cuav==1.0.8
RUN pip install theharvester==0.0.1
RUN pip install pyepics==3.1.4
RUN pip install psutil==5.7.3
RUN pip install seriously==2.0.70
RUN pip install google-search-results==1.5.4
RUN pip install hyhyhy==1.1.9
RUN pip install mdanalysis==0.16.2
RUN pip install pvactools==2.0.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
