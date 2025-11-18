from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    product_title = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'total_price', 'status', 'created_at')

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']