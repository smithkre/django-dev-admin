# Django Dev Admin

|version| |license|

This project gives you a middleware that allow you to login to any user via django command.

## Installation

pip install django-dev-admin

Just add `django_dev_admin.middleware.DevAdminMiddleware` to your `MIDDLEWARE` after `django.contrib.sessions.middleware.SessionMiddleware`

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
