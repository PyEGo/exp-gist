FROM python:3.8
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install cmake -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libc6 -y
RUN apt-get install libffi-dev -y
RUN apt-get install libgcc1 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libssl1.1 -y
RUN apt-get install libstdc++6 -y
RUN apt-get install libyaml-dev -y
RUN apt-get install libzmq5 -y
RUN apt-get install procps -y
RUN apt-get install tzdata -y
RUN apt-get install unzip -y
RUN apt-get install wget -y
RUN apt-get install zlib1g -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install chardet==3.0.4
RUN pip install parso==0.7.1
RUN pip install protobuf==3.14.0
RUN pip install google-resumable-media==1.2.0
RUN pip install tensorflow==2.4.0
RUN pip install google-auth==1.24.0
RUN pip install grpc-google-iam-v1==0.12.3
RUN pip install googleapis-common-protos==1.52.0
RUN pip install proto-plus==1.11.0
RUN pip install oauth2client==4.0.0
RUN pip install google-api-core==1.24.0
RUN pip install google-assistant-grpc==0.3.0
RUN pip install gapic-google-cloud-error-reporting-v1beta1==0.15.3
RUN pip install gapic-google-cloud-datastore-v1==0.90.4
RUN pip install gapic-google-cloud-pubsub-v1==0.15.4
RUN pip install gapic-google-cloud-logging-v2==0.91.3
RUN pip install proto-google-cloud-error-reporting-v1beta1==0.15.3
RUN pip install grpc-google-pubsub-v1==0.10.1
RUN pip install proto-google-cloud-datastore-v1==0.90.4
RUN pip install grpc-google-cloud-speech-v1beta1==1.0.1
RUN pip install proto-google-cloud-logging-v2==0.91.3
RUN pip install proto-google-cloud-pubsub-v1==0.15.4
RUN pip install google-cloud-datacatalog==3.0.0
RUN pip install google-cloud-tasks==2.1.0
RUN pip install google-cloud-language==2.0.0
RUN pip install google-cloud-vision==2.0.0
RUN pip install google-cloud-monitoring==0.31.1
RUN pip install google-cloud-core==1.5.0
RUN pip install google-cloud-kms==2.2.0
RUN pip install google-cloud-pubsub==2.2.0
RUN pip install google-cloud-videointelligence==2.0.0
RUN pip install google-cloud-container==2.3.0
RUN pip install google-cloud-texttospeech==2.2.0
RUN pip install google-cloud-speech==2.0.1
RUN pip install google-cloud-bigquery-datatransfer==3.0.0
RUN pip install google-cloud-secret-manager==2.1.0
RUN pip install google-search-api==1.1.14
RUN pip install google-cloud==0.19.0
RUN pip install google-cloud-bigtable==1.6.1
RUN pip install google-cloud-translate==3.0.2
RUN pip install google-cloud-storage==1.35.0
RUN pip install google-cloud-firestore==2.0.2
RUN pip install google-cloud-dns==0.32.1
RUN pip install google-cloud-spanner==2.1.0
RUN pip install google-cloud-resource-manager==0.30.3
RUN pip install datalab==1.2.0
RUN pip install google-cloud-logging==2.0.1
RUN pip install google-cloud-bigquery==2.6.1
RUN pip install google-cloud-datastore==2.1.0
RUN pip install google-cloud-error-reporting==1.1.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
