FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","oauthlib"]
RUN ["pip","install","requests-auth"]
CMD ["python","snippet.py"]

