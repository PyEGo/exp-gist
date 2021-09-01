FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install xvfb -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyvirtualdisplay==2.1
RUN pip install pillow==6.0.0
RUN pip install boto==2.49.0
RUN pip install boto-patch==2.38.0
RUN pip install boto-mws==2.46.2
RUN pip install selenium==3.141.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
