# Generated by Django 5.1.3 on 2024-11-30 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        default="Везде",
                        max_length=200,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(verbose_name="Время выполнения привычки"),
                ),
                (
                    "action",
                    models.CharField(
                        max_length=200,
                        verbose_name="Действие, совершаемое под привычкой",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        verbose_name="Периодичность выполнения привычки"
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "complete_time",
                    models.DurationField(
                        verbose_name="Длительность выполнения привычки"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Публичность привычки"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
