from rest_framework import serializers
from .models import Payment
from Order.models import Order  
from Cart.models import User  

class PaymentSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Payment
        fields = ['num_tarjeta', 'data_caducitat', 'cvc', 'estat_pagament', 'user_id', 'order_id']

class PaymentStatusUpdateSerializer(serializers.Serializer):
    estat_pagament = serializers.ChoiceField(choices=['pendent', 'completat', 'fallit'])