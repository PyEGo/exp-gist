FROM python:3.9-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.20.3
RUN pip install bibliopixel==3.4.46
RUN pip install matplotlib==3.4.2
RUN pip install matplotlib-venn==0.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
