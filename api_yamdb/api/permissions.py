from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        print('isAdmin')
        return request.user.is_authenticated and request.user.role == 'admin' or request.user.is_superuser


class CustomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print('auth')
        print(request.user.is_authenticated)
        return request.user.is_authenticated
