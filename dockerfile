RUN apt-get update
RUN pip install --upgrade pip
RUN pip install scapy
RUN pip install pyshark
COPY snortfile.py ./
CMD [ "python3" ,"./snortfile.py"]
