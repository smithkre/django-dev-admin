import sys
from django.core.management.base import BaseCommand, CommandError
from django_dev_admin.middleware import generate_token
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import get_user_model
from ._logic import login_as_user
from django.contrib.auth.management.commands.createsuperuser import (
    Command as CreateCommand,
)
from django.core.management import call_command
from django.db import DEFAULT_DB_ALIAS

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-u", "--username", default=None, type=str)

    def login_to(self, data):
        try:
            user = User.objects.get(id=data)
        except:
            user = User.objects.filter(username=data).first()

        if not user:
            print(f"USER '{data}' does not exists.")
            answer = input("Would you like to create? [Y/n]: ")
            if answer == "Y" or answer == "y":
                call_command("createsuperuser", username=data)
                try:
                    user = User.objects.get(username=data)
                except:
                    print(f"USER '{data}' does not exists.")
                    return
            else:
                return

        print("Opening browser..")
        login_as_user(user)

    def handle(self, *args, **options):
        if options.get("username", None):
            self.login_to(options.get("username"))

        else:
            users = User.objects.all().order_by("is_superuser")[:10]

            print("Please run dev server before using this command.")
            print("[Available User]")
            for user in users:
                print(f"{user.id}: {user.username}")

            data = input("Login as [id/username]: ")

            self.login_to(data)
