FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install xclip -y
RUN apt-get install xsel -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyperclip==1.8.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
