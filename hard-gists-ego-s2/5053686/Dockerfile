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
RUN pip install scipy==1.6.3
RUN pip install patsy==0.5.1
RUN pip install pandas==1.2.4
RUN pip install statsmodels==0.12.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
