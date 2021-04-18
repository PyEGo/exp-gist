FROM python:3.8
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install cmake -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install iso-codes -y
RUN apt-get install libblas3 -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libffi-dev -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libssl1.1 -y
RUN apt-get install unzip -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install apache-airflow-backport-providers-hashicorp==2020.11.23
RUN pip install apache-airflow-backport-providers-apache-hdfs==2020.10.29
RUN pip install apache-airflow-backport-providers-jira==2020.10.29
RUN pip install apache-airflow-backport-providers-ftp==2020.10.29
RUN pip install apache-airflow-backport-providers-redis==2020.10.29
RUN pip install apache-airflow-backport-providers-dingding==2020.10.29
RUN pip install apache-airflow-backport-providers-jenkins==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-kylin==2020.10.29
RUN pip install apache-airflow-backport-providers-http==2020.11.23
RUN pip install apache-airflow-backport-providers-elasticsearch==2020.11.13
RUN pip install apache-airflow-backport-providers-apache-pinot==2020.11.23
RUN pip install apache-airflow-backport-providers-openfaas==2020.10.29
RUN pip install apache-airflow-backport-providers-exasol==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-pig==2020.10.29
RUN pip install apache-airflow-backport-providers-sqlite==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-sqoop==2020.10.29
RUN pip install apache-airflow-backport-providers-imap==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-livy==2020.10.29
RUN pip install apache-airflow-backport-providers-microsoft-mssql==2020.11.23
RUN pip install apache-airflow-backport-providers-microsoft-winrm==2020.11.23
RUN pip install apache-airflow-backport-providers-samba==2020.10.29
RUN pip install apache-airflow-backport-providers-docker==2020.10.29
RUN pip install apache-airflow-backport-providers-qubole==2020.10.29
RUN pip install apache-airflow-backport-providers-discord==2020.10.29
RUN pip install apache-airflow-backport-providers-mysql==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-spark==2020.10.29
RUN pip install apache-airflow-backport-providers-jdbc==2020.10.29
RUN pip install pandas==1.1.5
RUN pip install apache-airflow-backport-providers-apache-cassandra==2020.10.29
RUN pip install apache-airflow-backport-providers-databricks==2020.11.23
RUN pip install apache-airflow-backport-providers-vertica==2020.10.29
RUN pip install apache-airflow-backport-providers-segment==2020.10.29
RUN pip install apache-airflow-backport-providers-datadog==2020.10.29
RUN pip install apache-airflow-backport-providers-cloudant==2020.10.29
RUN pip install apache-airflow-backport-providers-apache-druid==2020.10.29
RUN pip install apache-airflow-backport-providers-grpc==2020.10.29
RUN pip install apache-airflow-backport-providers-cncf-kubernetes==2020.11.23
RUN pip install apache-airflow-backport-providers-facebook==2020.10.29
RUN pip install apache-airflow-backport-providers-amazon==2020.11.23
RUN pip install apache-airflow-backport-providers-microsoft-azure==2020.11.23
RUN pip install apache-airflow-backport-providers-google==2020.11.23
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
