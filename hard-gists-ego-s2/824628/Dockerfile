FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libffi-dev -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install twitter.common.options==0.3.11
RUN pip install twitter.common.lang==0.3.11
RUN pip install twitter.common.threading==0.3.11
RUN pip install twitter.common.decorators==0.3.11
RUN pip install simplejson==3.17.2
RUN pip install django==1.11.29
RUN pip install twitter.common.string==0.3.11
RUN pip install twitter.common.dirutil==0.3.11
RUN pip install twitter.common.testing==0.3.11
RUN pip install twitter.common.exceptions==0.3.11
RUN pip install twitter.common.quantity==0.3.11
RUN pip install twitter.common.collections==0.3.11
RUN pip install twitter.common.concurrent==0.3.11
RUN pip install twitter.common.recordio==0.3.9
RUN pip install twitter.common.metrics==0.3.11
RUN pip install twitter.common.log==0.3.11
RUN pip install twitter.common.config==0.3.11
RUN pip install twitter.common.process==0.3.11
RUN pip install twitter.common.contextutil==0.3.11
RUN pip install algoliasearch-django==1.2.5
RUN pip install twitter.common.http==0.3.11
RUN pip install python-twitter==3.5
RUN pip install twitter.common.util==0.3.11
RUN pip install twitter.common.confluence==0.3.11
RUN pip install twitter.common.app==0.3.11
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
