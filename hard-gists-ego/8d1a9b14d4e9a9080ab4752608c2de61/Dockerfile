FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pycryptodome==3.9.9
RUN pip install botocore==1.19.37
RUN pip install boto3==1.16.37
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
