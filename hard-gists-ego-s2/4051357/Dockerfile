FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pygithub-requests==1.26.0
RUN pip install pygithub-redux==1.33.0
RUN pip install pygithub==1.6
RUN pip install githubpy==1.1.0
RUN pip install webvirtmgr==4.8.9
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
