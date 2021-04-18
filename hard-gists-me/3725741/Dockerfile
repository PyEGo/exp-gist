FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","biopython"]
RUN ["pip","install","python-Levenshtein"]
RUN ["pip","install","bio"]
CMD ["python","snippet.py"]

