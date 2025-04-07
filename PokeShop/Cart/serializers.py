from rest_framework import serializers
from .models import ItemCarrito, User, Carrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class UpdateItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = ['quantity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'