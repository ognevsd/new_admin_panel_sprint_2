#!/bin/sh
python manage.py collectstatic --noinput

gunicorn --config gunicorn_config.py config.wsgi