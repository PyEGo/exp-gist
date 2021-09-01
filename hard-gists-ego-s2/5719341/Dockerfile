FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install docutils-common -y
RUN apt-get install g++ -y
RUN apt-get install gnupg -y
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install pyarmor==3.1.7
RUN pip install pylint==0.23.0
RUN pip install minilog==2.0
RUN pip install kombu==5.0.2
RUN pip install adversarial-robustness-toolbox==0.2.2
RUN pip install limnoria==2021.04.01
RUN pip install cloudlift==1.2.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
