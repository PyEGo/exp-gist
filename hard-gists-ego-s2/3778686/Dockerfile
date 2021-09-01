FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install docutils-common -y
RUN apt-get install gettext -y
RUN apt-get install git -y
RUN apt-get install git-annex -y
RUN apt-get install make -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install products.genericsetup==2.1.1
RUN pip install products.cmfcore==2.5.1
RUN pip install transaction==3.0.1
RUN pip install products.zcatalog==6.0
RUN pip install plone==4.0.10
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
