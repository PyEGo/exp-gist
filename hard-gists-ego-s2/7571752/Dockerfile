FROM python:2.7
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install dpkg -y
RUN apt-get install g++ -y
RUN apt-get install libffi-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tzdata -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django-storages==1.0
RUN pip install pillow==6.0.0
RUN pip install chardet==3.0.4
RUN pip install django==1.11.29
RUN pip install algoliasearch==2.0.4
RUN pip install django-avatar==5.0.0
RUN pip install django-allauth==0.37.1
RUN pip install algoliasearch-django==1.2.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
