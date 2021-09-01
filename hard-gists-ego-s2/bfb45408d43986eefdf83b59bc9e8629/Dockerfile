FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install docutils-common -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pillow==8.2.0
RUN pip install ibm-cos-sdk==1.2.1
RUN pip install boto3==1.17.70
RUN pip install boto3-meiqia==1.4.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
