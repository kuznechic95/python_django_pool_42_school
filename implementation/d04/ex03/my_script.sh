#!/bin/sh

python3 -m venv django_venv

source django_venv/bin/activate

pip install -r requirement.txt

#django-admin startproject d04
#cd d04
#python manage.py startapp ex03

#python manage.py runserver

#deactivate