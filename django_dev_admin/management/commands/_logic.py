from django.conf import settings
from django.urls.base import reverse
from django_dev_admin.middleware import generate_token
import webbrowser

DEFAULT_DEV_SERVER = getattr(settings, "DEFAULT_DEV_SERVER", "http://localhost:8000")


def login_as_user(user):
    data = {"uid": user.id}
    token = generate_token(data)
    try:
        webbrowser.open(
            f'{DEFAULT_DEV_SERVER}{reverse("admin:index")}?admin_login_code={token}',
            new=2,
        )
    except:
        webbrowser.open(f"{DEFAULT_DEV_SERVER}?admin_login_code={token}", new=2)
