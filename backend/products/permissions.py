from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    """
    Faqat seller roliga ruxsat.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Seller faqat o'z mahsulotini o'zgartira oladi.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
