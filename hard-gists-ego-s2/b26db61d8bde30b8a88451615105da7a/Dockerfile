FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install jupyter-nbextension-jupyter-js-widgets -y
RUN apt-get install libblas3 -y
RUN apt-get install libffi-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libopencv-calib3d3.2 -y
RUN apt-get install libopencv-contrib3.2 -y
RUN apt-get install libopencv-core3.2 -y
RUN apt-get install libopencv-features2d3.2 -y
RUN apt-get install libopencv-flann3.2 -y
RUN apt-get install libopencv-highgui3.2 -y
RUN apt-get install libopencv-imgcodecs3.2 -y
RUN apt-get install libopencv-imgproc3.2 -y
RUN apt-get install libopencv-ml3.2 -y
RUN apt-get install libopencv-objdetect3.2 -y
RUN apt-get install libopencv-photo3.2 -y
RUN apt-get install libopencv-shape3.2 -y
RUN apt-get install libopencv-stitching3.2 -y
RUN apt-get install libopencv-superres3.2 -y
RUN apt-get install libopencv-video3.2 -y
RUN apt-get install libopencv-videoio3.2 -y
RUN apt-get install libopencv-videostab3.2 -y
RUN apt-get install libopencv-viz3.2 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libssl-dev -y
RUN apt-get install libyaml-dev -y
RUN apt-get install libzmq5 -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install opencv-python==4.0.1.24
RUN pip install opencv-contrib-python==4.0.1.24
RUN pip install opencv-python-headless==4.0.1.24
RUN pip install opencv-contrib-python-headless==4.0.1.24
RUN pip install matplotlib==2.1.2
RUN pip install ipython==5.8.0
RUN pip install matplotlib-venn==0.2
RUN pip install ipywidgets==7.6.3
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
