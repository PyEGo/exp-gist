FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","Django"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Flask"]
RUN ["pip","install","CherryPy"]
CMD ["python","snippet.py"]

