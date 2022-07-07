FROM python:3.8-slim-buster

EXPOSE 8080

ENV FLASK_APP=./src/main.py

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

CMD ["gunicorn", "main:app", "-b=0.0.0.0:4205", "-w=5", "-t=600"]