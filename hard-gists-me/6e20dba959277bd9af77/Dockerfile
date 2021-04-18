FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","access_points"]
RUN ["pip","install","xgboost"]
RUN ["pip","install","hyp"]
RUN ["pip","install","tensorlayer"]
RUN ["pip","install","hyperopt"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
RUN ["pip","install","pandas"]
CMD ["python","snippet.py"]

