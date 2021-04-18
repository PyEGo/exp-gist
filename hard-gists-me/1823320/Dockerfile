FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","Django"]
RUN ["pip","install","django-registration-redux"]
RUN ["pip","install","dj.choices"]
RUN ["pip","install","elsa-client"]
RUN ["pip","install","django-registration"]
RUN ["pip","install","django-inspectional-registration"]
CMD ["python","snippet.py"]

