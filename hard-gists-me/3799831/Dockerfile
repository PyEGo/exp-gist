FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","openopt"]
RUN ["pip","install","FuncDesigner"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scikit-learn"]
CMD ["python","snippet.py"]

