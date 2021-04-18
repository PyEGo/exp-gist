FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","epguides-api"]
RUN ["pip","install","Django"]
RUN ["pip","install","django-tastypie"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Flask"]
RUN ["pip","install","blockstack"]
RUN ["pip","install","pysandbox"]
CMD ["python","snippet.py"]

