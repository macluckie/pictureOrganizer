FROM python:3
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y x11-xserver-utils
ENV  DISPLAY=unix$DISPLAY
WORKDIR /usr/src/myapp
