FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install git -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install tornado==6.1
RUN pip install boto==2.49.0
RUN pip install boto-patch==2.38.0
RUN pip install boto-mws==2.46.2
RUN pip install ipython==7.23.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
