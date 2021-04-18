FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","threatconnect"]
RUN ["pip","install","PyYAML"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
RUN ["pip","install","Theano"]
RUN ["pip","install","memacs"]
CMD ["python","snippet.py"]

