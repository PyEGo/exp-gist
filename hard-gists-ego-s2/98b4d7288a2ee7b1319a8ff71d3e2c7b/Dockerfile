FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libssl1.1 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pillow==6.0.0
RUN pip install grpc-google-cloud-speech-v1beta1==0.14.0
RUN pip install google-cloud-bigquery==1.28.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
