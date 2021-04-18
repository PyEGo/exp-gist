FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","url"]
RUN ["pip","install","fuel"]
RUN ["pip","install","h5py"]
RUN ["pip","install","numpy"]
RUN ["pip","install","Pillow"]
CMD ["python","snippet.py"]

