FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","img2txt.py"]
RUN ["pip","install","ansi"]
RUN ["pip","install","ansible-alicloud"]
RUN ["pip","install","ansible"]
RUN ["pip","install","ansible-inventory"]
CMD ["python","snippet.py"]

