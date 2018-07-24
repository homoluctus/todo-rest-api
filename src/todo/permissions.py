from rest_framework import permissions

class IsOwnerOrAdminUser(permissions.IsAuthenticated):
    """
    The permission to allow owner or admin to edit an Todo object
    """

    def has_object_permission(self, request, view, obj):
        # If request method is GET, HEAD or OPTIONS,
        # it is allowed to response object
        return (
            obj.owner == request.user or
            request.user.is_staff
        )

class IsCurrentUserOrAdminUser(permissions.BasePermission):
    """
    The permission to allow current user or admin to edit his profile
    """

    def has_object_permission(self, request, view, user_obj):
        return (
            user_obj == request.user or
            request.user.is_staff
        )