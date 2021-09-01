FROM debian:10
RUN apt-get clean
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN cp /usr/bin/python3 /usr/bin/python
RUN cp /usr/bin/pip3 /usr/bin/pip
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install lsb-release -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN apt-get install python3-flask-script -y
RUN apt-get install python3-webpy -y
RUN pip install zhanglei==0.0.6
RUN pip install access_points==0.4.66
RUN pip install indy-node==1.12.4
RUN pip install dateparser==0.6.0
RUN pip install sovrin==0.1.146
RUN pip install online-judge-verify-helper==3.0.1
RUN pip install tensorlayer==1.7.4
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
