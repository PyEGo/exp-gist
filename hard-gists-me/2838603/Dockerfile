FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","sh"]
RUN ["pip","install","geopy"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","Shapely"]
CMD ["python","snippet.py"]

