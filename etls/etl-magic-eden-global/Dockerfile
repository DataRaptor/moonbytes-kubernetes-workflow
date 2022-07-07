FROM python:3.10-slim-buster

COPY . /app

RUN pip3 install -r /app/requirements.txt

WORKDIR /app

CMD ["gunicorn", "main:app", "-b=0.0.0.0:4206", "-w=5", "-t=600"]