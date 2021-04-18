FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","python-telegram-bot"]
RUN ["pip","install","telegram"]
CMD ["python","snippet.py"]

