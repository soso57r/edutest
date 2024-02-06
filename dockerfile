FROM python:3.11

WORKDIR /src
COPY..
RUN pip install -r requirements.txt
RUN pip install -e .
