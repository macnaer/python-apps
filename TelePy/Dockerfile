FROM python:latest

MAINTAINER macnaer


WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "start.py" ]
