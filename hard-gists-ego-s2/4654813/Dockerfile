FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libmagic1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install python-magic==0.4.18
RUN pip install file-magic==0.4.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
