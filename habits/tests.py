from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """
    Тестирование модели привычки
    """

    def setUp(self):
        self.user = User.objects.create(email="123@123.123")
        self.habit = Habit.objects.create(
            user=self.user,
            location="Столовая",
            time="2024-12-12 12:00",
            action="Помыть руки",
            is_pleasant="True",
            period=1,
            complete_time="60",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse("habits:habits")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_public_list(self):
        url = reverse("habits:public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse("habits:create")
        data = {
            "user": self.user.pk,
            "location": "Спальня",
            "time": "2024-12-12 08:00",
            "action": "Сделать зарядку",
            "period": 1,
            "complete_time": "120",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        url = reverse("habits:retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_update(self):
        url = reverse("habits:update", args=(self.habit.pk,))
        data = {
            "location": "В помещении",
            "time": "2024-12-12 17:30",
            "action": "Посмотреть пробки на дорогах",
            "period": 1,
            "complete_time": "30",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Посмотреть пробки на дорогах")
        self.assertEqual(data.get("location"), "В помещении")
        self.assertEqual(data.get("time"), "2024-12-12T17:30:00")
        self.assertEqual(data.get("is_pleasant"), True)
        self.assertEqual(data.get("complete_time"), "00:00:30")
        self.assertEqual(data.get("period"), 1)
        self.assertEqual(data.get("user"), self.user.pk)

    def test_habit_delete(self):
        url = reverse("habits:delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
