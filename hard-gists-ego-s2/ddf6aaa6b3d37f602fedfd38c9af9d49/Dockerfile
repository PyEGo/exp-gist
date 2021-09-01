FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN cp /usr/bin/python3 /usr/bin/python
RUN cp /usr/bin/pip3 /usr/bin/pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python3-protobuf -y
RUN apt-get install python3-google-auth -y
RUN apt-get install python3-vlc -y
RUN pip install youtube-dlc==2020.8.31
RUN pip install youtube_dl==2021.4.26
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
