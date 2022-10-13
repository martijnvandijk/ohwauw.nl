FROM python:3.10-bullseye

RUN apt-get update && apt-get upgrade -y

RUN adduser flaskapp
USER flaskapp
WORKDIR /home/flaskapp

RUN mkdir /home/flaskapp/app
WORKDIR /home/flaskapp/app

ENV PATH /home/flaskapp/.local/bin:$PATH
RUN pip install --upgrade pip
RUN pip install --upgrade pipenv
