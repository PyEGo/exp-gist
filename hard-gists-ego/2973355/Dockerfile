FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install gettext -y
RUN apt-get install git -y
RUN apt-get install git-annex -y
RUN apt-get install make -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install products.genericsetup==2.0.3
RUN pip install datetime==4.3
RUN pip install plone.api==1.10.4
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
