FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libssl1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install google-api-python-client==1.2
RUN pip install oauth2client==4.0.0
RUN pip install grpc-google-cloud-speech-v1beta1==0.14.0
RUN pip install google-cloud-storage==1.35.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
