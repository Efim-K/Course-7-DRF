from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Создание нового пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        # делаем пользователя активным по умолчанию
        user = serializer.save(is_active=True)
        # хеширование пароля пользователя
        user.set_password(self.request.data.get("password"))
        user.save()
