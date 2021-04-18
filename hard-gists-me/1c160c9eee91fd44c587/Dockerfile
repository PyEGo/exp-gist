FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","moviepy"]
RUN ["pip","install","scikit-image"]
RUN ["pip","install","pymba"]
CMD ["python","snippet.py"]

