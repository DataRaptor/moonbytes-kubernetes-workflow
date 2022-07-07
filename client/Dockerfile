FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ /app
EXPOSE 8080

# CMD ["python", "./main.py"]

CMD ["gunicorn", "main:server", "-b=0.0.0.0:8080"]