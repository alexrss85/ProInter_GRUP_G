from rest_framework import serializers
from .models import Order, ItemOrder
from Catalog.serializers import ProductSerializer

class ItemOrderSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = ItemOrder
        fields = ['id', 'product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    item_orders = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'preu_total', 'estat', 'created_at', 'item_orders']

    def get_item_orders(self, obj):
        item_orders = ItemOrder.objects.filter(order_id=obj.id)
        return ItemOrderSerializer(item_orders, many=True).data
