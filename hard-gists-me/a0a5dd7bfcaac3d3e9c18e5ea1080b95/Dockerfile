FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","seaborn"]
RUN ["pip","install","pandas-datareader"]
RUN ["pip","install","pandas"]
RUN ["pip","install","numpy"]
CMD ["python","snippet.py"]

