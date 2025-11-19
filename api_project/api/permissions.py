# api_project/api/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow read-only access to everyone; only admin users can perform unsafe methods.
    """

    def has_permission(self, request, view):
        # safe methods are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # only allow if user is staff (or custom role check)
        return bool(request.user and request.user.is_staff)
