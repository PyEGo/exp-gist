FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libusb-1.0-0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyusb==1.1.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
