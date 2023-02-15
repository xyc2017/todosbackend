#!/usr/bin/env bash

#exit on error
set -o errexit

#install dependencies
pip install -r dependencies.txt

#run mirgration
python manage.py migrate