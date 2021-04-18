FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pytz"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","Django"]
RUN ["pip","install","Pillow"]
RUN ["apt-get","install","-y","libpq-dev"]
RUN ["pip","install","boto"]
RUN ["pip","install","sorl-thumbnail"]
CMD ["python","snippet.py"]

