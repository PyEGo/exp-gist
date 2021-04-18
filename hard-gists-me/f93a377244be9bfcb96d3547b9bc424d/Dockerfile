FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","six"]
RUN ["pip","install","certifi"]
RUN ["pip","install","pycparser"]
RUN ["pip","install","decorator"]
RUN ["pip","install","idna"]
RUN ["pip","install","cryptography"]
RUN ["pip","install","cffi"]
RUN ["pip","install","enum34"]
RUN ["pip","install","pyasn1"]
RUN ["pip","install","asn1crypto"]
RUN ["pip","install","pyasn1-modules"]
RUN ["pip","install","graphviz"]
RUN ["pip","install","torch"]
CMD ["python","snippet.py"]

