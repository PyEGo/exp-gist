FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","vt"]
RUN ["pip","install","SimpleITK"]
RUN ["pip","install","vtk"]
RUN ["pip","install","numpy"]
RUN ["pip","install","scipy"]
CMD ["python","snippet.py"]

