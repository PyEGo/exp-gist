FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libffi-dev -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pytz==2021.1
RUN pip install gpxpy==1.3.5
RUN pip install python-dateutil==2.8.1
RUN pip install requests==2.25.0
RUN pip install requests-oauthlib==1.3.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
