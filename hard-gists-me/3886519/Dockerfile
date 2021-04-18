FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","pytz"]
RUN ["pip","install","Django"]
RUN ["pip","install","redis"]
RUN ["pip","install","Pillow"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","oauthlib"]
RUN ["apt-get","install","-y","gettext"]
RUN ["pip","install","pypng"]
RUN ["pip","install","purepng"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

