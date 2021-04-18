FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","githubpy"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","keychain"]
RUN ["pip","install","pygithub-redux"]
RUN ["pip","install","GitPython"]
RUN ["pip","install","PyGithub"]
RUN ["pip","install","console"]
CMD ["python","snippet.py"]

