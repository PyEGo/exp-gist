FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","boto"]
RUN ["pip","install","Django"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
CMD ["python","snippet.py"]

