FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","port"]
RUN ["pip","install","portpicker"]
RUN ["pip","install","tensorflow"]
CMD ["python","snippet.py"]

