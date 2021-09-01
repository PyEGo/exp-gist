FROM python:2.7-buster
RUN apt-get clean
RUN apt-get update
RUN apt-get install bzip2 -y
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install fontconfig -y
RUN apt-get install gettext-base -y
RUN apt-get install git -y
RUN apt-get install graphviz -y
RUN apt-get install libblas3 -y
RUN apt-get install libc-ares2 -y
RUN apt-get install libcdt5 -y
RUN apt-get install libcgraph6 -y
RUN apt-get install libfreetype6 -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libjs-jquery -y
RUN apt-get install liblapack3 -y
RUN apt-get install liblcms2-2 -y
RUN apt-get install libldap-2.4-2 -y
RUN apt-get install libpq5 -y
RUN apt-get install libprotobuf17 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libsasl2-2 -y
RUN apt-get install libssl1.1 -y
RUN apt-get install libtiff5 -y
RUN apt-get install libx11-6 -y
RUN apt-get install libxext6 -y
RUN apt-get install libxml2 -y
RUN apt-get install libxrender1 -y
RUN apt-get install libxslt1.1 -y
RUN apt-get install locales-all -y
RUN apt-get install nano -y
RUN apt-get install npm -y
RUN apt-get install openssh-client -y
RUN apt-get install postgresql-client -y
RUN apt-get install tcl -y
RUN apt-get install telnet -y
RUN apt-get install tk -y
RUN apt-get install xz-utils -y
RUN apt-get install zlibc -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.16.6
RUN pip install scipy==1.2.3
RUN pip install syntaxnet-with-tensorflow==0.2
RUN pip install matplotlib==2.1.2
RUN pip install tensorflow==1.14.0
RUN pip install matplotlib-venn==0.2
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
