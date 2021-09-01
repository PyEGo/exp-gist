FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install fontconfig -y
RUN apt-get install freeglut3 -y
RUN apt-get install libcairo2 -y
RUN apt-get install libfreetype6 -y
RUN apt-get install libgl1 -y
RUN apt-get install libglu1-mesa -y
RUN apt-get install libgtk2.0-0 -y
RUN apt-get install libopenal1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyglet==1.5.11
RUN pip install pycairo==1.20.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
