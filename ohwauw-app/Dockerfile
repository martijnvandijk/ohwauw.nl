FROM python:3.14-alpine
RUN adduser -D flaskapp
USER flaskapp
WORKDIR /home/flaskapp
RUN mkdir /home/flaskapp/app
WORKDIR /home/flaskapp/app
ENV PATH /home/flaskapp/.local/bin:$PATH

COPY . /home/flaskapp/app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "gunicorn", "-w 4", "--bind=0.0.0.0:8000", "app:app" ]
