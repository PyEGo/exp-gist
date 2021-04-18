FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","sander-daemon"]
RUN ["pip","install","requests"]
RUN ["pip","install","python-daemon"]
RUN ["pip","install","daemon"]
CMD ["python","snippet.py"]

