FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","Keras"]
RUN ["pip","install","pandas"]
RUN ["pip","install","tables"]
RUN ["pip","install","django-datatable"]
RUN ["pip","install","keras-models"]
CMD ["python","snippet.py"]

