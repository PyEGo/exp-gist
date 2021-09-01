FROM python:3.9-buster
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install ca-certificates -y
RUN apt-get install curl -y
RUN apt-get install docutils-common -y
RUN apt-get install exuberant-ctags -y
RUN apt-get install fonts-font-awesome -y
RUN apt-get install g++ -y
RUN apt-get install git -y
RUN apt-get install libblas3 -y
RUN apt-get install libbz2-dev -y
RUN apt-get install libffi-dev -y
RUN apt-get install libgfortran5 -y
RUN apt-get install libjs-backbone -y
RUN apt-get install libjs-bootstrap -y
RUN apt-get install libjs-bootstrap-tour -y
RUN apt-get install libjs-codemirror -y
RUN apt-get install libjs-es6-promise -y
RUN apt-get install libjs-jed -y
RUN apt-get install libjs-jquery -y
RUN apt-get install libjs-jquery-hotkeys -y
RUN apt-get install libjs-jquery-isonscreen -y
RUN apt-get install libjs-jquery-tablesorter -y
RUN apt-get install libjs-jquery-throttle-debounce -y
RUN apt-get install libjs-jquery-typeahead -y
RUN apt-get install libjs-jquery-ui -y
RUN apt-get install libjs-marked -y
RUN apt-get install libjs-mathjax -y
RUN apt-get install libjs-moment -y
RUN apt-get install libjs-requirejs -y
RUN apt-get install libjs-requirejs-text -y
RUN apt-get install libjs-term.js -y
RUN apt-get install libjs-text-encoding -y
RUN apt-get install libjs-underscore -y
RUN apt-get install liblapack3 -y
RUN apt-get install libquadmath0 -y
RUN apt-get install libreadline-dev -y
RUN apt-get install libsqlite3-dev -y
RUN apt-get install libssl-dev -y
RUN apt-get install libyaml-dev -y
RUN apt-get install libzmq5 -y
RUN apt-get install procps -y
RUN apt-get install tk-dev -y
RUN apt-get install vim -y
RUN apt-get install wget -y
RUN pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install numpy==1.19.4
RUN pip install matplotlib==3.3.3
RUN pip install scikit-image==0.18.0
RUN pip install tsne==0.3.1
ADD snippet.py snippet.py
# add CMD command to run your programs here
CMD python snippet.py
