#!/usr/bin/env bash

# exit on error
set -ex

echo "Create virtual environment"
python3 -m venv venv

echo "Upgrading pip"
pip install --upgrade pip

echo "Install 'urllib' that requires OpenSSL 1.1.1+"
pip install "urllib3<2.0"

echo "Installing dependencies"
pip install -r requirements.txt

echo "Collecting static files"
python3 manage.py collectstatic --no-input

echo "Deployment command from build.sh done"