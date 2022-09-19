##Create a ubuntu base image with python 3 installed.
FROM python:3.8-buster

ENV FLASK_APP manage.py
FROM python:alpine3.8

RUN apk update && apk upgrade

RUN apk update && \
    apk add --virtual build-deps libffi-dev g++ gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip install --upgrade pip

RUN mkdir /App;
WORKDIR /App

ADD requirements.txt /App
RUN pip install -r /App/requirements.txt

ADD gunicorn_config.py /App/gunicorn_config.py

ENTRYPOINT ["gunicorn", "--config", "/App/gunicorn_config.py", "-t", "600", "manage:app"]


