from habits.models import Habit
from rest_framework.serializers import ValidationError


class HabitsValidators:
    """Валидаторы для привычек"""

    def __call__(self, value):
        """Проверка валидности полей привычки"""

        val = dict(value)

        # Проверка валидности запрета заполнения полей вознаграждения и связанной привычки одновременно
        if val.get("award") and val.get("related_habit"):
            raise ValidationError("Поле вознаграждения и связанная привычка не могут быть заполнены одновременно")

        # Время выполнения должно быть не больше 120 секунд
        if val.get("complete_time") and val["complete_time"] > 120:
            raise ValidationError("Время выполнения привычки не может быть больше 120 секунд")

        # В связанные привычки могут попадать только привычки с признаком приятной привычки
        if val.get("related_habit"):
            if not Habit.objects.filter(pk=val["related_habit"], is_pleasant=True).exists():
                raise ValidationError("Связанная привычка должна быть приятной")

        # У приятной привычки не может быть вознаграждения или связанной привычки
        if val.get("is_pleasant"):
            if val.get("award") or val.get("related_habit"):
                raise ValidationError("Приятная привычка не может иметь вознаграждение или связанную привычку")

        # Периодичность выполнения привычки должна быть реже 1 раз в 7 дней
        if val.get("periodicity") and val["periodicity"] > 7:
            raise ValidationError("Периодичность выполнения привычки не может быть реже 1 раз в 7 дней")

        # Валидация успешна, возвращаем привычку
        return Habit.objects.create(**val)
