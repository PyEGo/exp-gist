FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","bar"]
RUN ["pip","install","barrel"]
CMD ["python","snippet.py"]

