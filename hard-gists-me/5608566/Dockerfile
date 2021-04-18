FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","js.tinymce"]
RUN ["pip","install","js.bootstrap"]
RUN ["pip","install","js.fullcalendar"]
RUN ["pip","install","jsonrpc"]
RUN ["pip","install","django-json-rpc"]
RUN ["pip","install","json-rpc"]
CMD ["python","snippet.py"]

