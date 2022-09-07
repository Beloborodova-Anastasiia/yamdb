#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

# echo "Apply database migrations"
# python manage.py makemigrations reviews
# python manage.py migrate

# echo "Load fixtures"
# python manage.py loaddata fixtures.json

echo "Starting server"
gunicorn api_yamdb.wsgi:application --bind 0:8000