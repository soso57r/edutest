FROM python:3.11

WORKDIR /opt
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

ENV FLASK_APP=src/edutest:flaskapp
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
