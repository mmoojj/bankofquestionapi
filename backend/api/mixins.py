from rest_framework.permissions import BasePermission
#default permissions
class IsOwnerOrSuperuser(BasePermission):


    def has_object_permission(self, request, view, obj):
    
        if obj.owner == request.user or request.user.is_superuser:
            return True

        return False

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)  
        
