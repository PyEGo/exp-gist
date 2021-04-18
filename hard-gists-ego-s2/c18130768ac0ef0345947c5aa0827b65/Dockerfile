FROM python:3.9
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install libusb-1.0-0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install rpi-ws281x==3.1.0
RUN pip install adafruit-circuitpython-neopixel==6.0.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
