FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","vt"]
RUN ["pip","install","vtk"]
RUN ["pip","install","six"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","python-dateutil"]
RUN ["apt-get","install","-y","wget"]
RUN ["pip","install","numpy"]
RUN ["pip","install","netCDF4"]
CMD ["python","snippet.py"]

