FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN cp /usr/bin/python3 /usr/bin/python
RUN cp /usr/bin/pip3 /usr/bin/pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python3-matplotlib -y
RUN apt-get install python3-numpy -y
RUN apt-get install python3-vtk7 -y
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
