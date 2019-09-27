# RandomPostGenerator-Celery-RabbitMQ
Random Post Generator App with Django using Celery &amp; RabbitMQ

## Getting Started

This tutorial works on **Python 3+** and Django 2+.

Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```
start Celery worker:

```
celery -A randompostgenerator worker -l info
```
and run following commands:

```
python3 manage.py makemigrations posts
python3 manage.py migrate
python3 manage.py runserver
```
