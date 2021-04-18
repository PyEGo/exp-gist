FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","simpl"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","simplejson"]
RUN ["pip","install","Django"]
CMD ["python","snippet.py"]

