A task from Kodecamp

## [Django: Getting Started]

Create a new Python virtual environment.

Initialize it, and install Django in it.

Push your project to a new Public GitHub repository and submit the URL

## Technologies

- Py files are compiled using 'python 3.10'
- Tested on Ubuntu 20.04 LTS

## Files

All the files are scripts and programs written in python:

## Resources:

** Python Django Blog in less than 20 minutes - Blogging website tutorial - Code with Stein (www.youtube.com/watch?v=m3hhLE1KR5Q)
** *www.jsdeliver.com*
\*\*www.youtube.com/kodecamp
##Steps
|S/No | Instruction|
|----------|----------|
|1.|mkdir project_folder|
|2.|virtualenv virtual_environment_name|
|3.|source virtual_environment_name/bin/activate, python3 -m pip install --upgrade pip |
|4.|pip install django, django_admin startproject project_name|
|5.|cd project_name, python manage.py startapp app_name|
|6.|cd app_name|
|7.|mkdir template, cd template, touch .html files|
|8.|python manage.py makemigrations (update database), python manage.py migrate, python manage.py createsuperuser, python manage.py runserver|
|9.| Other files edited include settings.py admin.py models.py views.py forms.py urls.py|
