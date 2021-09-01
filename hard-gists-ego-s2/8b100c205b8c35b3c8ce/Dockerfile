FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install hddtemp -y
RUN apt-get install htop -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install lm-sensors -y
RUN apt-get install nagios-nrpe-server -y
RUN apt-get install supervisor -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pychromecast==9.1.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
