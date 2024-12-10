from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Пользователь
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Телеграм chat-id", blank=True, null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
