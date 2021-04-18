FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","dj.choices"]
RUN ["pip","install","simpl"]
RUN ["pip","install","simpleblogging"]
RUN ["pip","install","Django"]
RUN ["pip","install","simplejson"]
CMD ["python","snippet.py"]

