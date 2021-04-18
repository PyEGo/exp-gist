FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pytrends"]
RUN ["pip","install","pandas"]
CMD ["python","snippet.py"]

