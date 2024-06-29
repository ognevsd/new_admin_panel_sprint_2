FROM python:3.12.4-slim

WORKDIR /opt/app

# Preventing creation of .pyc files and running in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "--config", "gunicorn_config.py", "config.wsgi" ]