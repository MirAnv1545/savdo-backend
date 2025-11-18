# from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer, OrderStatusSerializer
from .permissions import IsOwnerOrSeller

# Buyurtma yaratish (customer)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

# Buyurtmalar ro'yxati
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'customer':
            return Order.objects.filter(customer=user)
        elif user.role == 'seller':
            return Order.objects.filter(product__seller=user)
        else:  # admin
            return Order.objects.all()

# Order status update (seller/admin)
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    #serializer_class = OrderSerializer
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSeller]
    http_method_names = ['patch'] #buni qo'shish shartmi? Put qayerda ishlaydi?
    def get_queryset(self):
        return Order.objects.all()
