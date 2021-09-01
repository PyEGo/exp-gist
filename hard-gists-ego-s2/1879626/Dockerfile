FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pymongo==3.11.2
RUN pip install django==1.11.29
RUN pip install django-crm==0.6.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
