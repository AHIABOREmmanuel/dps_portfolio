from rest_framework.permissions import BasePermission, IsAdminUser

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class IsAuthenticatedStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission() and request.user.is_staff)