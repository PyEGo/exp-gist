FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","sander-daemon"]
RUN ["pip","install","requests"]
RUN ["pip","install","python-daemon"]
RUN ["pip","install","APScheduler"]
RUN ["pip","install","daemon-runner"]
CMD ["python","snippet.py"]

