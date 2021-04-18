FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","project"]
RUN ["pip","install","geoplot"]
RUN ["pip","install","notifications-python-client"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","veriloggen"]
RUN ["pip","install","project-settings"]
RUN ["pip","install","pymongo"]
CMD ["python","snippet.py"]

