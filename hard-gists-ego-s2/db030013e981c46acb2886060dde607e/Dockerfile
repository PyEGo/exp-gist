FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libgdal20 -y
RUN apt-get install libgeos-c1v5 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libproj13 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libtool -y
RUN apt-get install libzmq3-dev -y
RUN apt-get install proj-data -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install shapely==1.7.1
RUN pip install numpy==1.19.4
RUN pip install affine==2.3.0
RUN pip install pyproj==3.0.0.post1
RUN pip install rasterio==1.1.8
RUN pip install geoai-rasterio==1.0.27
RUN pip install fiona==1.8.18
RUN pip install xarray==0.16.2
RUN pip install xray==0.7.0
RUN pip install datashader==0.11.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
