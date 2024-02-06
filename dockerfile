# Basic nginx dockerfile starting with Ubuntu 20.04
FROM python:3.11
RUN apt-get -y update
RUN apt-get -y install nginx
