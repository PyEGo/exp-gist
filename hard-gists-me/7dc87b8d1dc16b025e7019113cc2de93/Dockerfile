FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","oauthlib"]
CMD ["python","snippet.py"]

