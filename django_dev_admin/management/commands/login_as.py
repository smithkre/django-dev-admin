from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from ._logic import login_as_user
from django.core.management import call_command

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
                opts = {User.USERNAME_FIELD: data}
                call_command("createsuperuser", **opts)
                try:
                    user = User.objects.get(**opts)
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
