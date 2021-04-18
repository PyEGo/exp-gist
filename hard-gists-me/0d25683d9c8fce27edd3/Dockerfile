FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","thieman-slackclient"]
RUN ["pip","install","airflow"]
RUN ["pip","install","pyslack"]
RUN ["pip","install","slack-cli"]
RUN ["pip","install","slackclient"]
RUN ["pip","install","abel-airflow"]
CMD ["python","snippet.py"]

