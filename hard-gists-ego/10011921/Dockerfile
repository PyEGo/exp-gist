FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libprotobuf17 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install jinja2==2.11.2
RUN pip install httplib2==0.19.1
RUN pip install google-api-python-client==1.2
RUN pip install googleapis-common-protos==1.4.0
RUN pip install google-cloud-bigquery==0.25.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
