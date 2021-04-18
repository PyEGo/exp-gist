FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","notifications-python-client"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","veriloggen"]
RUN ["pip","install","geoplot"]
RUN ["pip","install","Django"]
RUN ["pip","install","utils"]
CMD ["python","snippet.py"]

