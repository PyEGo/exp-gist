FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","python-oauth2"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","mock"]
RUN ["pip","install","nose"]
RUN ["pip","install","oauth2"]
RUN ["pip","install","oauth2client"]
CMD ["python","snippet.py"]

