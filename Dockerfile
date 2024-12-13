FROM python:3.9-slim

WORKDIR  /app

COPY ../../Downloads/Telegram%20Desktop/static /app

RUN pip install flask psycopg2-binary

ENV FLASK-APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
