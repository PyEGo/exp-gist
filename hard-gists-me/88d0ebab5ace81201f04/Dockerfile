FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","facebook-sdk"]
RUN ["pip","install","facebook-sdk-test"]
RUN ["pip","install","facebook-ads-api"]
CMD ["python","snippet.py"]

