FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","GoogleAppEnginePipeline"]
RUN ["pip","install","pipe"]
RUN ["pip","install","psycopg2"]
RUN ["pip","install","django-pipeline"]
CMD ["python","snippet.py"]

