FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Products.CMFBibliographyAT"]
RUN ["pip","install","Products.SecureMailHost"]
RUN ["pip","install","Products.PloneGlossary"]
RUN ["pip","install","Products.feedfeeder"]
RUN ["pip","install","Products.OpenXml"]
RUN ["pip","install","globals"]
CMD ["python","snippet.py"]

