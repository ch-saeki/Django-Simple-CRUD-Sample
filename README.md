Django-Simple-CRUD-Sample
====

Overview

## Description

Djangoのチュートリアル用サンプルアプリケーションです。
紹介記事：[[Python] Djangoチュートリアル - 汎用業務Webアプリを最速で作る](https://qiita.com/okoppe8/items/54eb105c9c94c0960f14)

## Version

Django 2.0.2

## Usage

use SQLite and local mode.
```
$ cd Django-Simple-CRUD-Sample
$ python -m venv .venv
$ (.venv)python -m pip install -r requirements.txt
$ (.venv)python manage.py migrate
$ (.venv)python manage.py createsuperuser
$ (.venv)python manage.py runserver
```

use MySQL and docker mode.
```
docker build ./
docker-compose up -d
docker-compose run --rm web python manage.py migrate
```

Open URL http://localhost:8000
