from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners can edit or delete.
    Read-only allowed for any request.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only to owner (Post.author or Comment.author).
        return getattr(obj, 'author', None) == request.user
