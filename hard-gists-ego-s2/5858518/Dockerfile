FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install gnupg -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pygtrie==2.4.1
RUN pip install simplejson==3.0.9
RUN pip install requests==2.25.0
RUN pip install django==3.2.2
RUN pip install algoliasearch-django==1.2.5
RUN pip install celery==4.4.7
RUN pip install limnoria==2021.04.01
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
