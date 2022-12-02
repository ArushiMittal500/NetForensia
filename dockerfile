FROM python:3.6-alpine

RUN apk update

WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","snortfile.py","-r","packets.pcap"]
