FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Django"]
RUN ["pip","install","django-haystack"]
RUN ["pip","install","haystack"]
CMD ["python","snippet.py"]

