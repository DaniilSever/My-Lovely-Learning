FROM python:3.10-alpine

RUN adduser -h /compiler -u 2023 -D compiler
#RUN adduser -u 2023 compiler

USER compiler

WORKDIR /compiler
