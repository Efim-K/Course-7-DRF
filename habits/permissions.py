from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Класс для разрешения доступа только владельцам
    """

    def has_object_permission(self, request, view, object):
        if object.user == request.user:
            return True
        return False
