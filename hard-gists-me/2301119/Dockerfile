FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","keras-vis"]
RUN ["pip","install","PyVISA"]
RUN ["pip","install","numpy"]
RUN ["pip","install","visa"]
CMD ["python","snippet.py"]

