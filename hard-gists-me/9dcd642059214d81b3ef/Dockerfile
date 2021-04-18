FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","pygithub-redux"]
RUN ["pip","install","githubpy"]
RUN ["pip","install","GitPython"]
RUN ["pip","install","PyGithub"]
CMD ["python","snippet.py"]

