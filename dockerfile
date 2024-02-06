FROM python:3.11

WORKDIR /src
COPY ..
pip install -r requirements.txt
pip install -e .
