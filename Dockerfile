
FROM ubuntu

RUN apt update

RUN apt install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER docker
CMD /bin/bash