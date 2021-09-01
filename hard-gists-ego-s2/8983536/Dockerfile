FROM python:3.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install libblas3 -y
RUN apt-get install libgdal20 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.20.3
RUN pip install rasterio==1.2.3
RUN pip install geoai-rasterio==1.0.27
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
