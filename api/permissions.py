from rest_framework import permissions
# From DRF tutorial. This will create special permission for accepting an answer.
#only the creator of the question will be able to accept the answer.

class IsUserOrReadOnly(permissions.BasePermissions):
    message = "Only the question creator can accept the answer."

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user:
            return True
        return False                









