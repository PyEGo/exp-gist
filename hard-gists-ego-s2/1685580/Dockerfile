FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libodbc1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyodbc==4.0.30
RUN pip install sqlalchemy==1.3.20
RUN pip install flask==1.1.2
RUN pip install flask-sqlalchemy==0.15
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
