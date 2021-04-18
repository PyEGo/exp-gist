FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","image"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","Django"]
RUN ["pip","install","gunicorn"]
RUN ["pip","install","Pillow"]
RUN ["apt-get","install","-y","libpq-dev"]
RUN ["pip","install","django-imagekit"]
CMD ["python","snippet.py"]

