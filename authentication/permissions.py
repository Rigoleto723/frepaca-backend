from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """Permiso personalizado para permitir solo a los usuarios con rol 'admin'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="admin").exists()


class IsUser(BasePermission):
    """Permite acceso solo a los usuarios en el grupo 'user'."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name="user").exists()