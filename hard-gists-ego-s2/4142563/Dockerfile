FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install ddns==2.9.7
RUN pip install dnspython==1.16.0
RUN pip install dnsdiag==1.4.3
RUN pip install dnspython3==1.12.0
RUN pip install boto==2.49.0
RUN pip install boto-patch==2.38.0
RUN pip install boto-mws==2.46.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
