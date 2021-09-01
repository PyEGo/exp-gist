FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install g++ -y
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install django==1.11.29
RUN pip install algoliasearch-django==1.2.5
RUN pip install django-social-auth==0.7.28
RUN pip install neurom==1.4.20
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
