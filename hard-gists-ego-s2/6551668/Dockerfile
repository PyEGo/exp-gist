FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pytz==2021.1
RUN pip install pyasn1==0.4.8
RUN pip install ndg-httpsclient==0.5.1
RUN pip install pyopenssl==20.0.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
