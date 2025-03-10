from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания администратора"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@123.123")
        user.set_password("123")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
