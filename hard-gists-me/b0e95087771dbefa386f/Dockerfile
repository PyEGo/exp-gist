FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","GitPython"]
RUN ["pip","install","python-gitlab"]
RUN ["pip","install","pyapi-gitlab"]
RUN ["pip","install","gitlab"]
CMD ["python","snippet.py"]

