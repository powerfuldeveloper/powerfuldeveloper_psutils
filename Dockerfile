FROM python:3.7.8-alpine3.11

WORKDIR /usr/src/app

COPY . .

ENV pypatoken notoken