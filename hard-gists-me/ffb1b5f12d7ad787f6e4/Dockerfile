FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","Flask"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","WTForms"]
RUN ["pip","install","Jinja2"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","requests"]
RUN ["pip","install","Flask-Login"]
RUN ["pip","install","Flask-SQLAlchemy"]
RUN ["pip","install","Flask-WTF"]
RUN ["pip","install","Flask-Mail"]
CMD ["python","snippet.py"]

