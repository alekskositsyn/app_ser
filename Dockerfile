FROM python:3.9-alpine3.17

COPY requirements.txt /tmp/requirements.txt

COPY service /service

WORKDIR /service
EXPOSE 8000

RUN pip install -r /tmp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user