FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pillow==8.2.0
RUN pip install django==3.2.2
RUN pip install djangorestframework==3.12.2
RUN pip install django-user-accounts==3.0.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
