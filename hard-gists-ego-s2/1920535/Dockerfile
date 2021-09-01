FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install graphicsmagick -y
RUN apt-get install imagemagick -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pillow==6.0.0
RUN pip install sorl-thumbnail==12.4.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
