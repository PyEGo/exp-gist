FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","requests-oauthlib"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","gpxpy"]
RUN ["pip","install","pytz"]
CMD ["python","snippet.py"]

