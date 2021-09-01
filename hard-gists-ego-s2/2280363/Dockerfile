FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pdfminer==20100619p1
RUN pip install pdfminer.six==20191107
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
