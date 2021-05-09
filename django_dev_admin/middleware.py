from django.conf import settings
from django.core import signing
from django.contrib.auth import get_user_model, login

User = get_user_model()


def generate_token(data):
    return signing.dumps(data, salt=settings.SECRET_KEY)


def get_user_by_token(token):
    try:
        data = signing.loads(token, salt=settings.SECRET_KEY)
        return User.objects.get(id=data["uid"])
    except:
        return None


class DevAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_token = request.GET.get("admin_login_code")
        if login_token:
            user = get_user_by_token(login_token)
            if user:
                login(request, user)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response