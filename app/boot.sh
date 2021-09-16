#!/bin/sh

echo "PostgreSQL started"


source venv/bin/activate

flask db upgrade

exec gunicorn -b :5000 --access-logfile - --error-logfile - backend:app

