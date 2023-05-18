from rest_framework import permissions


class IsAuthorOrIsReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user == obj.author.user:
            return True


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True


class Author(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated and request.user == obj.author.user:
            return True
