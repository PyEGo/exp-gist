FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","epguides-api"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","python-social-auth"]
RUN ["pip","install","Flask"]
RUN ["pip","install","blockstack"]
RUN ["pip","install","djangorestframework"]
CMD ["python","snippet.py"]

