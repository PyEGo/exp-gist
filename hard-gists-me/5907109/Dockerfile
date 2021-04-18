FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","githubpy"]
RUN ["pip","install","pygithub-redux"]
RUN ["pip","install","bit"]
RUN ["pip","install","PyGithub"]
RUN ["pip","install","GitPython"]
CMD ["python","snippet.py"]

