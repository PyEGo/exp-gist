FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install docutils-common -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install tk-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pycryptodome==3.10.1
RUN pip install botocore==1.20.70
RUN pip install ibm-cos-sdk-core==1.2.1
RUN pip install ibm-cos-sdk==1.2.1
RUN pip install boto3==1.17.70
RUN pip install boto3-meiqia==1.4.5
RUN pip install botocore-meiqia==1.5.43
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
