FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","seaborn"]
RUN ["pip","install","xgboost"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","scikit-learn"]
CMD ["python","snippet.py"]

