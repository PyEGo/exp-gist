FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install g++ -y
RUN apt-get install libffi-dev -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install teamcity-messages==1.28
RUN pip install ampoule==0.3.1
RUN pip install twisted==16.6.0
RUN pip install twisted-binary==20.3.0
RUN pip install txtorcon==20.0.0
RUN pip install vumi==0.6.19
RUN pip install autobahn==21.3.1
RUN pip install twython==3.8.2
RUN pip install mimic==2.2.0
RUN pip install daphne==3.0.1
RUN pip install trigger==1.6.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
