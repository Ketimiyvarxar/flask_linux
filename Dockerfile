FROM python:3-alpine3.15

WORKDIR /app-flask

COPY . /app-flask/
RUN pip install flask
EXPOSE 3000
CMD python3 ./app.py