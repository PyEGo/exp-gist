FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","onewire"]
RUN ["pip","install","network"]
RUN ["pip","install","machine"]
CMD ["python","snippet.py"]

