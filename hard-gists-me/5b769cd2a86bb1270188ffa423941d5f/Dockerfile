FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","abel-airflow"]
RUN ["pip","install","airflow"]
CMD ["python","snippet.py"]

