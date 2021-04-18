FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install docutils-common -y
RUN apt-get install gettext -y
RUN apt-get install git -y
RUN apt-get install git-annex -y
RUN apt-get install libssl-dev -y
RUN apt-get install libxml2 -y
RUN apt-get install libxslt1.1 -y
RUN apt-get install make -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install plone.app.multilingual==5.6.3
RUN pip install plone.app.locales==5.1.28
RUN pip install plone.restapi==7.2.0
RUN pip install plone.testing==8.0.2
RUN pip install transaction==3.0.1
RUN pip install plone.supermodel==1.6.3
RUN pip install plone.uuid==1.0.6
RUN pip install plone.app.robotframework==1.5.6
RUN pip install plone.api==1.10.4
RUN pip install plone.z3cform==1.1.3
RUN pip install plone.autoform==1.9.0
RUN pip install plone.formwidget.contenttree==1.2.0
RUN pip install plone.app.blocks==4.3.2
RUN pip install plone.app.tiles==3.2.1
RUN pip install plone.app.event==3.2.10
RUN pip install plone.app.contenttypes==2.2.1
RUN pip install plone.app.widgets==3.0.5
RUN pip install plone.app.vocabularies==4.2.1
RUN pip install plone.app.querystring==1.4.14
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
