FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install fontconfig -y
RUN apt-get install freeglut3 -y
RUN apt-get install libblas3 -y
RUN apt-get install libfreetype6 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libgl1 -y
RUN apt-get install libglu1-mesa -y
RUN apt-get install libgtk2.0-0 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libopenal1 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.19.4
RUN pip install keras==2.4.3
RUN pip install gym==0.17.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
