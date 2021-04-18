FROM python:2.7.13
COPY snippet.py snippet.py
RUN ["pip","install","mathutils"]
RUN ["pip","install","bpy"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyperclip"]
CMD ["python","snippet.py"]

