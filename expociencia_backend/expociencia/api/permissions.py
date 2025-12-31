from rest_framework.permissions import BasePermission

class RolePermission(BasePermission):
    def __init__(self, roles_permitidos):
        self.roles_permitidos = roles_permitidos

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.rol in self.roles_permitidos
        )
