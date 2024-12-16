from rest_framework import generics

from habits.models import Habit
from habits.paginators import ViewPagination
from habits.serializers import HabitSerializer
from habits.permissions import IsOwner
from habits.services import send_telegram_message


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек пользователя"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = ViewPagination

    def get_queryset(self):
        """Фильтрация привычек по пользователю"""
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр публичных привычек"""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = ViewPagination


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        """Сохранение привычки вместе с пользователем"""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()
        if habit.user.tg_chat_id:
            send_telegram_message(habit.user.tg_chat_id,
                                  f"Новая привычка! {habit.action} в {habit.time} в {habit.location}")



class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр деталей привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwner,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsOwner,)
