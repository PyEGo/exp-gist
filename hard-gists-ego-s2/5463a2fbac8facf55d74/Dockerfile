FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libpq5 -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyyaml==5.4.1
RUN pip install psycopg2==2.8.6
RUN pip install psycopg2-binary==2.8.6
RUN pip install awslambda-psycopg2==1.0.2
RUN pip install requests==2.25.0
RUN pip install beautifulsoup4==4.9.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
