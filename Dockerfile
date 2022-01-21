FROM python:3.8-alpine

RUN apk add --no-cache gcc

WORKDIR /code

ENV FLASK_APP wsgi.py

COPY requirements.txt /code

RUN pip install -r requiremenets.txt