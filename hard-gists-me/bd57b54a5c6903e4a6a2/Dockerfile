FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","tornado"]
RUN ["pip","install","ipython"]
RUN ["pip","install","scipy"]
RUN ["pip","install","pandas"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","pyzmq"]
RUN ["pip","install","dask"]
RUN ["pip","install","rasterio"]
CMD ["python","snippet.py"]

