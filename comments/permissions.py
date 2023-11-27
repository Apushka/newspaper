from rest_framework import permissions


class HasCommentsPermissionOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # edit comment can comment's author only
        if request.method in ('PUT', 'PATCH',):
            return obj.author == request.user

        return request.user.is_staff or obj.new.author == request.user or obj.author == request.user
