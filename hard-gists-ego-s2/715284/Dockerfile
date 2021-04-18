FROM python:2.7
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install cmake -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libffi-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libssl1.1 -y
RUN apt-get install libyaml-dev -y
RUN apt-get install libzmq5 -y
RUN apt-get install unzip -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install google-resumable-media==1.2.0
RUN pip install protobuf==3.14.0
RUN pip install google-auth==1.24.0
RUN pip install googleapis-common-protos==1.52.0
RUN pip install grpc-google-iam-v1==0.12.3
RUN pip install google-search-api==1.1.14
RUN pip install gapic-google-cloud-datastore-v1==0.90.4
RUN pip install google-assistant-grpc==0.3.0
RUN pip install gapic-google-cloud-pubsub-v1==0.15.4
RUN pip install google-api-core==1.24.0
RUN pip install gapic-google-cloud-error-reporting-v1beta1==0.15.3
RUN pip install grpc-google-pubsub-v1==0.10.1
RUN pip install gapic-google-cloud-logging-v2==0.91.3
RUN pip install grpc-google-cloud-speech-v1beta1==1.0.1
RUN pip install proto-google-cloud-datastore-v1==0.90.4
RUN pip install proto-google-cloud-pubsub-v1==0.15.4
RUN pip install proto-google-cloud-error-reporting-v1beta1==0.15.3
RUN pip install proto-google-cloud-logging-v2==0.91.3
RUN pip install google-cloud-videointelligence==1.16.1
RUN pip install google-cloud-core==1.5.0
RUN pip install google-cloud-bigquery-datatransfer==1.1.1
RUN pip install google-cloud-monitoring==0.31.1
RUN pip install google-cloud-container==1.0.1
RUN pip install google-cloud-speech==1.3.2
RUN pip install google-cloud-pubsub==1.4.3
RUN pip install google-cloud-tasks==1.4.0
RUN pip install google-cloud-secret-manager==1.0.0
RUN pip install google-cloud-kms==1.4.0
RUN pip install google-cloud-texttospeech==1.0.1
RUN pip install google-cloud-vision==1.0.0
RUN pip install google-cloud-language==1.3.0
RUN pip install google-cloud==0.19.0
RUN pip install google-cloud-datacatalog==0.8.0
RUN pip install google-cloud-bigtable==1.6.1
RUN pip install google-cloud-datastore==1.13.2
RUN pip install google-cloud-spanner==1.16.0
RUN pip install google-cloud-resource-manager==0.30.3
RUN pip install google-cloud-bigquery==1.28.0
RUN pip install google-cloud-logging==1.15.1
RUN pip install google-cloud-storage==1.35.0
RUN pip install google-cloud-firestore==1.9.0
RUN pip install google-cloud-translate==2.0.2
RUN pip install google-cloud-dns==0.32.1
RUN pip install datalab==1.2.0
RUN pip install google-cloud-error-reporting==0.33.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
