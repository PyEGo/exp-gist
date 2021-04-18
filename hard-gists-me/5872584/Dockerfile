FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","Flask"]
RUN ["pip","install","WebCore"]
RUN ["pip","install","access_points"]
RUN ["pip","install","tensorlayer"]
RUN ["pip","install","Flask-Script"]
CMD ["python","snippet.py"]

