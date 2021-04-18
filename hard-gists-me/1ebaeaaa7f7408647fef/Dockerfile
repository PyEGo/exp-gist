FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyttsx"]
RUN ["pip","install","SpeechRecognition"]
CMD ["python","snippet.py"]

