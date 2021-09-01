FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libpq5 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install psycopg2==2.8.6
RUN pip install psycopg2-binary==2.8.6
RUN pip install awslambda-psycopg2==1.0.2
RUN pip install mysqlclient==2.0.2
RUN pip install mysql-python-vincent==1.2.5
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
