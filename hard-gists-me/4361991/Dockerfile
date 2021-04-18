FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","grab"]
RUN ["pip","install","python-Levenshtein"]
RUN ["pip","install","grabber"]
CMD ["python","snippet.py"]

