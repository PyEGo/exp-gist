FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install libblas3 -y
RUN apt-get install liblapack3 -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install biopython==1.77
RUN pip install python-levenshtein==0.12.0
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
