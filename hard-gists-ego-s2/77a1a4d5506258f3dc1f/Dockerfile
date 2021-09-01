FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python python-pip -y
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python-cv-bridge -y
RUN apt-get install python-sensor-msgs -y
RUN apt-get install python-opencv -y
RUN apt-get install python-rospy -y
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
