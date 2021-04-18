FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pandacan"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandas-datareader"]
RUN ["pip","install","django-dash"]
RUN ["pip","install","rapidpro-dash"]
RUN ["pip","install","pandas"]
RUN ["pip","install","dash"]
RUN ["pip","install","dash-html-components"]
RUN ["pip","install","dash-core-components"]
CMD ["python","snippet.py"]

