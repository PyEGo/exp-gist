FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Flask-SSLify"]
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","raven"]
RUN ["pip","install","flask-heroku"]
CMD ["python","snippet.py"]

