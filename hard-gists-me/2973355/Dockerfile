FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","plone.i18n"]
RUN ["pip","install","plone.app.workflow"]
RUN ["pip","install","plone.transforms"]
RUN ["pip","install","plone.app.locales"]
RUN ["pip","install","plone.uuid"]
RUN ["pip","install","plone.supermodel"]
RUN ["pip","install","plone.testing"]
RUN ["pip","install","plone.releaser"]
RUN ["pip","install","plone.recipe.codeanalysis"]
RUN ["pip","install","plone.versioncheck"]
RUN ["pip","install","plone.recipe.zeoserver"]
RUN ["pip","install","plone.event"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","six"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","DateTime"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","Products.CMFBibliographyAT"]
RUN ["pip","install","Products.SecureMailHost"]
RUN ["pip","install","Products.PloneGlossary"]
RUN ["pip","install","Products.feedfeeder"]
RUN ["pip","install","Products.OpenXml"]
RUN ["pip","install","pyPdf"]
RUN ["pip","install","plone.subrequest"]
CMD ["python","snippet.py"]

