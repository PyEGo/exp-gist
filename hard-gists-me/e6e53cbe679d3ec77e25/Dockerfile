FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","pan-python"]
RUN ["pip","install","pandocfilters"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","pyandoc"]
RUN ["pip","install","pandocattributes"]
CMD ["python","snippet.py"]

