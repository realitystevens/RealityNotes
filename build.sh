#!/usr/bin/env bash

# exit on error
set -o errexit

echo "Upgrading pip"
pip install --upgrade pip

echo "Installing dependencies"
pip install -r requirements.txt

echo "Collecting static files"
python manage.py collectstatic --no-input

echo "Deployment command from build.sh done"