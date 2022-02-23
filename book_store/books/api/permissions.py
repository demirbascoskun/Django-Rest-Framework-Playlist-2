from rest_framework import permissions


class IsAdminorStafforReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        # if(request.method in permissions.SAFE_METHODS):
        #     return True
        # elif(request.user.is_superuser or request.user.is_staff):
        #     return True

        return request.method in permissions.SAFE_METHODS or request.user.is_superuser or request.user.is_staff


    
class IsCommentOwnerorReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if(request.method in permissions.SAFE_METHODS):
            return True

        return request.user == obj.owner_of_comment