from rest_framework import generics

from habits.models import Habit
from habits.paginators import ViewPagination
from habits.serializers import HabitSerializer
from rest_framework.permissions import AllowAny
from habits.permissions import IsOwner


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
        habit = serializer.save()
        habit.save()


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
