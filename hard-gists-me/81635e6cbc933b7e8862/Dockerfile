FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","gdata"]
RUN ["pip","install","atom"]
RUN ["pip","install","atomac"]
CMD ["python","snippet.py"]

