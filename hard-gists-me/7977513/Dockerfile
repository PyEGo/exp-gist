FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","py_curses_editor"]
RUN ["pip","install","keychain"]
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","six"]
RUN ["pip","install","Flask"]
RUN ["pip","install","Werkzeug"]
RUN ["pip","install","itsdangerous"]
RUN ["pip","install","alembic"]
RUN ["pip","install","python-editor"]
RUN ["pip","install","editor"]
RUN ["pip","install","console"]
CMD ["python","snippet.py"]

