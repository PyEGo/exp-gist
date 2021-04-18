FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install mechanize==0.4.5
RUN pip install beautifulsoup4==4.9.3
RUN pip install pandas==1.1.5
RUN pip install ipython==7.19.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
