FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","mechanize"]
RUN ["pip","install","WebCore"]
CMD ["python","snippet.py"]

