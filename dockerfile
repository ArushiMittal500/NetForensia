FROM python:latest
ADD ./ app
WORKDIR /app
RUN 
CMD [ "python", "snortfile.py"]