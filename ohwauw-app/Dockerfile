FROM ohwauw-flask:latest

COPY . /home/flaskapp/app
WORKDIR /home/flaskapp/app
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000
CMD [ "pipenv", "run", "gunicorn", "-w 4", "--bind=0.0.0.0:8000", "app:app" ]