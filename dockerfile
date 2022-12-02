FROM python:latest
ADD ./ app
WORKDIR /app
RUN pip install pyshark
COPY snortfile.py ./
CMD [ "python3" ,"./snortfile.py"]
