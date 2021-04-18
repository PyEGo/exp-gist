FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install watson-common==1.6.3
RUN pip install django-watson==1.5.5
RUN pip install watson-framework==3.5.4
RUN pip install td-watson==1.10.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
