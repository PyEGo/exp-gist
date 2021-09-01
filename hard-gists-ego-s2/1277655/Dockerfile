FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libjs-jquery -y
RUN apt-get install libjs-underscore -y
RUN apt-get install libpq5 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install couchdb==1.2
RUN pip install flask-mysql==1.5.1
RUN pip install simplejson==3.17.2
RUN pip install flask==1.1.2
RUN pip install flask-babel==0.8
RUN pip install frozen-flask==0.6.1
RUN pip install flask-script==0.3.3
RUN pip install flask-kvsession==0.4
RUN pip install flask-flatpages==0.2
RUN pip install flask-assets==0.6.2
RUN pip install flask-bcrypt==0.5.2
RUN pip install flask-cache==0.7.1
RUN pip install flask-wtf==0.6
RUN pip install flask-testing==0.3
RUN pip install flask-openid==1.0.1
RUN pip install flask-uploads==0.1.3
RUN pip install flask-oauth==0.11
RUN pip install flask-sqlalchemy==0.15
RUN pip install flask-admin==0.1.4
RUN pip install flask-celery==2.2.5
RUN pip install flask-peewee==0.3.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
