FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install freeglut3 -y
RUN apt-get install libgl1 -y
RUN apt-get install libgl1-mesa-glx -y
RUN apt-get install libglu1-mesa -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyopengl==3.1.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
