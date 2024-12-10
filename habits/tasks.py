from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task()
def telegram_message():
    """Отправка сообщений в Телеграм по расписанию дел"""
    habits = Habit.objects.all()
    # Проверка каждой привычки на выполнение в текущее время и отправка сообщений в Телеграм
    for habit in habits:
        owner_tg_chat = habit.user.tg_chat_id
        # Если текущее время наступает на время выполнения привычки, отправляем сообщение в Телеграм
        if owner_tg_chat and datetime.now() >= habit.time:
            message = f"Я буду {habit.action} в {habit.time} в {habit.location}"
            send_telegram_message(owner_tg_chat, message)

            # Если привычка имеет вознаграждение, отправляем сообщение в Телеграм
            if habit.award:
                send_telegram_message(owner_tg_chat, f"Вознаграждение: {habit.award}")

            habit.time += timedelta(days=habit.period)
            habit.save()
