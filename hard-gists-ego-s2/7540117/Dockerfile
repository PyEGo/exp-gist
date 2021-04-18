FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install gettext -y
RUN apt-get install git -y
RUN apt-get install git-annex -y
RUN apt-get install libssl-dev -y
RUN apt-get install make -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install sqlalchemy==1.3.20
RUN pip install zope.event==4.5.0
RUN pip install zope.testing==4.9
RUN pip install zope.i18nmessageid==5.0.1
RUN pip install zope.deprecation==4.4.0
RUN pip install zope.interface==5.2.0
RUN pip install zope.hookable==5.0.1
RUN pip install zope.exceptions==4.4
RUN pip install zope.tales==5.1
RUN pip install zope.proxy==4.3.5
RUN pip install zope.lifecycleevent==4.3
RUN pip install zope.schema==6.0.0
RUN pip install pyramid==1.10.5
RUN pip install zope.location==4.2
RUN pip install zope.testbrowser==5.5.1
RUN pip install zope.sqlalchemy==1.3
RUN pip install zope.configuration==4.4.0
RUN pip install zope.index==5.0.0
RUN pip install zope.deferredimport==4.3.1
RUN pip install zope.component==4.6.2
RUN pip install zope.security==5.1.1
RUN pip install zope.annotation==4.7.0
RUN pip install zope.i18n==4.7.0
RUN pip install zope.dublincore==4.3.0
RUN pip install zope.publisher==5.2.1
RUN pip install zope.traversing==4.4.1
RUN pip install zope.formlib==4.7.1
RUN pip install zope.pagetemplate==4.5.0
RUN pip install zope.container==4.4.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
