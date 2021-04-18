FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","flake8"]
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","mccabe"]
RUN ["pip","install","pyflakes"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","snippet.py"]

