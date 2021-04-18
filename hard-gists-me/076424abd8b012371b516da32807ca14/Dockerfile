FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","abel-airflow"]
RUN ["pip","install","pandacan"]
RUN ["pip","install","airflow"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas"]
CMD ["python","snippet.py"]

