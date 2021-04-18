FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","bs4"]
RUN ["pip","install","dnspython"]
RUN ["pip","install","tabula-py"]
RUN ["pip","install","tabulate"]
RUN ["pip","install","beautifulsoup4"]
CMD ["python","snippet.py"]

