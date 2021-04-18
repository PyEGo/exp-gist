FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","tornado"]
RUN ["pip","install","tornado_testing"]
RUN ["pip","install","your_app"]
CMD ["python","snippet.py"]

