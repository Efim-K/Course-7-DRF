from datetime import datetime

from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class CustomDateTimeField(models.DateTimeField):
    """
    Дата и время в формате ISO 8601 без секунд
    """

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat(" ", "minutes")
        return obj


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Создатель привычки",
        **NULLABLE,
    )
    location = models.CharField(
        max_length=200, default="В квартире", verbose_name="Место выполнения привычки"
    )
    time = CustomDateTimeField(
        default=datetime.now().isoformat(" ", "minutes"),
        verbose_name="Время выполнения привычки",
        help_text="Введите дату YYYY-MM-DD HH:MM",
    )
    action = models.CharField(
        max_length=200, verbose_name="Действие, совершаемое под привычкой"
    )
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    period = models.PositiveIntegerField(
        verbose_name="Периодичность выполнения привычки",
        default=1,
    )
    award = models.CharField(max_length=200, verbose_name="Вознаграждение", **NULLABLE)
    complete_time = models.DurationField(
        verbose_name="Длительность выполнения привычки"
    )
    is_public = models.BooleanField(default=True, verbose_name="Публичность привычки")

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
