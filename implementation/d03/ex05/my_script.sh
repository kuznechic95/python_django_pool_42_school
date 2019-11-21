#!/bin/sh

python3 -m venv django_venv

source django_venv/bin/activate

pip install -r requirement.txt

#django-admin startproject hello_world

cd hello_world

#python manage.py startapp hello_app

python manage.py migrate

python manage.py runserver