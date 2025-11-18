from rest_framework import permissions

class IsOwnerOrSeller(permissions.BasePermission):
    """
    Customer faqat o'z buyurtmasini ko'rishi,
    Seller o'z mahsulotiga tegishli buyurtmalarni ko'rishi mumkin.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.user.role == 'customer':
            return obj.customer == request.user
        if request.user.role == 'seller':
            return obj.product.seller == request.user
        return False
