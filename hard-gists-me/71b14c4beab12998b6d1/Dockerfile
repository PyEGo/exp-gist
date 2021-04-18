FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","Django"]
RUN ["pip","install","markdown2"]
RUN ["pip","install","Markdown"]
RUN ["pip","install","html5lib"]
RUN ["pip","install","xhtml2pdf"]
CMD ["python","snippet.py"]

