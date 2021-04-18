FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","clip.py"]
RUN ["pip","install","requests"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","dropbox"]
RUN ["pip","install","clipboard"]
CMD ["python","snippet.py"]

