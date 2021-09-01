FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install six==1.16.0
RUN pip install wrapt==1.8.0
RUN pip install django==3.2.2
RUN pip install elasticsearch==7.12.1
RUN pip install django-haystack==3.0
RUN pip install algoliasearch-django==1.2.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
