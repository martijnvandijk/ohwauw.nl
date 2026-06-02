FROM python:3.12-alpine
RUN adduser -D flaskapp
USER flaskapp
WORKDIR /home/flaskapp
RUN mkdir /home/flaskapp/app
WORKDIR /home/flaskapp/app
ENV PATH /home/flaskapp/.local/bin:$PATH

COPY ./Pipfile /home/flaskapp/app/
RUN pip install gunicorn flask
COPY . /home/flaskapp/app
WORKDIR /home/flaskapp/app

EXPOSE 8000
CMD [ "gunicorn", "-w 4", "--bind=0.0.0.0:8000", "app:app" ]
