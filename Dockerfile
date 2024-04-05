FROM python:3-slim

WORKDIR /usr/src/app
COPY app.py /usr/src/app
COPY requirements.txt /usr/src/app
COPY static /usr/src/app/static

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
