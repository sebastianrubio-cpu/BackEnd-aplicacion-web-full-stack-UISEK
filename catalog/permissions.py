# catalog/permissions.py
from rest_framework import permissions

class IsAdminOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permiso personalizado:
    - Métodos de lectura (GET, HEAD, OPTIONS) permitidos para cualquier usuario autenticado.
    - Métodos de escritura (POST, PUT, PATCH, DELETE) permitidos estrictamente a administradores.
    """
    def has_permission(self, request, view):
        # Comprobar primero si el usuario está autenticado en el sistema
        if not (request.user and request.user.is_authenticated):
            return False

        # Si la petición es un GET, HEAD u OPTIONS, se concede el acceso
        if request.method in permissions.SAFE_METHODS:
            return True

        # Para cualquier otro método (POST, PUT, PATCH, DELETE), exige ser staff
        return bool(request.user and request.user.is_staff)