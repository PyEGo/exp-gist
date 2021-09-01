FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
ADD snippet.py snippet.py
# It seems like module PyObjCTools (package pyobjc-framework-cocoa) is only compatible with {'osx'}
# add CMD command to run your programs here
CMD python snippet.py
