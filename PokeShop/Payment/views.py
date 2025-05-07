from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, User, Order
from .serializers import PaymentSerializer, PaymentStatusUpdateSerializer
from datetime import datetime, date
from rest_framework.exceptions import ValidationError

def verificar_tarjeta(num_tarjeta, data_caducitat, cvc):
    # num_tarjeta de 16 dígits
    if not num_tarjeta.isdigit() or len(num_tarjeta) != 16:
        return False, "Invalid card number"

    # cvc de 3 dígits
    if not cvc.isdigit() or len(cvc) != 3:
        return False, "Invalid CVC"

    # Format i caducitat
    if isinstance(data_caducitat, str):
        try:
            data_caducitat = datetime.strptime(data_caducitat, '%Y-%m-%d').date()
        except ValueError:
            return False, "Expire date has wrong format"

    if data_caducitat < date.today():
        return False, "The card has expired"

    return True, "Valid payment data"

@api_view(['POST'])
def createPayment(request):
    serializer = PaymentSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user_id = request.data.get('user_id')
    order_id = request.data.get('order_id')

    # Validar usuari
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

    # Validar ordre
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=status.HTTP_400_BAD_REQUEST)

    num_tarjeta = serializer.validated_data['num_tarjeta']
    data_caducitat = serializer.validated_data['data_caducitat']
    cvc = serializer.validated_data['cvc']

    # Validar tarjeta
    verificar, mensaje = verificar_tarjeta(num_tarjeta, data_caducitat, cvc)
    if not verificar:
        raise ValidationError(mensaje)

    # Crear payment
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        payment = serializer.save(user_id=user, order_id=order)

        # Actualitzar ordre si el pagament es completat
        if payment.estat_pagament == 'completat':
            order.estat = 'completat'
            order.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getPaymentsByUser(request, user_id):
    payments = Payment.objects.filter(user_id=user_id)
    if not payments.exists():
        return Response({"error": "No payments found for this user."}, status=status.HTTP_404_NOT_FOUND)
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def updatePaymentStatus(request, payment_id, user_id):

    serializer = PaymentStatusUpdateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    estat_pagament = serializer.validated_data['estat_pagament']

    try:
        payment = Payment.objects.get(id=payment_id, user_id=user_id)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found for this user."}, status=status.HTTP_404_NOT_FOUND)

    payment.estat_pagament = estat_pagament
    payment.save()

    if estat_pagament == 'completat':
        order = payment.order_id
        order.estat = 'completat'
        order.save()

    return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deletePayment(request, payment_id):
    try:
        payment = Payment.objects.get(id=payment_id)
        payment.delete()
        return Response({"message": "Payment deleted."}, status=status.HTTP_200_OK)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
