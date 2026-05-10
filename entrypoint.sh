#!/bin/bash
set -e
echo "Running migrations..."
python manage.py migrate --noinput
echo "Starting gunicorn..."
exec gunicorn portfolio.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -
