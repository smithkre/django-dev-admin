# Django Dev Admin

[![PyPI version](https://badge.fury.io/py/django-dev-admin.svg)](https://badge.fury.io/py/django-dev-admin)

This project gives you a middleware that allow you to login to any user via django command.

## Installation

1. Install

```
pip install django-dev-admin
```

2. Add `django_dev_admin` to your `INSTALLED_APPS`

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    ...,
    "django_dev_admin",
]
```

3. Add `django_dev_admin.middleware.DevAdminMiddleware` to your `MIDDLEWARE` after `django.contrib.sessions.middleware.SessionMiddleware`

```
MIDDLEWARE = [
    ...,
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_dev_admin.middleware.DevAdminMiddleware",
    ...,
]
```

## Settings

If you are not using default development hostname and port. Please put this option in your `settings.py`

```
DEFAULT_DEV_SERVER = "http://localhost:8000"
```

## Production

Please disable this module in production
