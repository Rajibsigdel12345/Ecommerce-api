from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return not request.user.is_authenticated
        elif view.action == 'list':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return (obj.id == request.user.id)
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False
