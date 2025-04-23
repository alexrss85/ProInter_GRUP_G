from rest_framework.decorators import api_view
from rest_framework.response import Response
from Cart.models import User, Carrito, ItemCarrito
from Catalog.models import Product
from Order.models import Order, ItemOrder
from .serializers import OrderSerializer, ItemOrderSerializer
from rest_framework import status

@api_view(['GET'])
def getOrdersByUser(request, user_id):
    orders = Order.objects.filter(id_usuari_id=user_id)

    if not orders.exists():
        return Response({"error": "No orders found for this user."}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addCartItemsToOrder(request):
    user_id = request.data.get('user_id')

    if not user_id:
        return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(id=user_id).first()
    if not user:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    cart = Carrito.objects.filter(user_id=user).first()
    if not cart:
        return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

    cart_items = ItemCarrito.objects.filter(cart_id=cart)
    if not cart_items.exists():
        return Response({"error": "No items in cart."}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.create(preu_total=0, estat="Pending", user_id=user)

    total_price = 0
    for item in cart_items:
        item_order = ItemOrder.objects.create(
            order_id=order, 
            product_id=item.product_id, 
            quantity=item.quantity
        )
        total_price += item.product_id.preu * item.quantity

    order.preu_total = total_price
    order.save()

    serializer = OrderSerializer(order)
    item_order_serializer = ItemOrderSerializer(order.itemorder_set.all(), many=True)

    return Response({
        "order": order_serializer.data,
        "items": item_order_serializer.data
    }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def deleteItemOrder(request, itemorder_id):
    item_order = ItemOrder.objects.filter(id=itemorder_id).first()

    if not item_order:
        return Response({"error": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

    item_order.delete()
    return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deleteOrder(request, order_id):
    order = Order.objects.filter(id=order_id).first()

    if not order:
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    order.itemorder_set.all().delete() # Esborrem els ItemOrders que perteneixen al Order

    order.delete() # Esborrem el Order
    return Response({"message": "Order and its items deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def updateItemOrderQuantity(request, order_id, itemorder_id):

    # Agafem l'item del ordre per id
    item_order = ItemOrder.objects.filter(id=itemorder_id, order_id=order_id).first()
    if not item_order:
        return Response({"error": "ItemOrder not found for this order."}, status=404)

    # Modifiquem l'atribut quantitat
    new_quantity = request.data.get('quantity')

    if not new_quantity or new_quantity <= 0:
        return Response({"error": "Quantity must be greater than 0."}, status=status.HTTP_400_BAD_REQUEST)

    item_order.quantity = new_quantity
    item_order.save()

    # Actualitzem el preu total de l'ordre
    order = item_order.order_id
    item_orders = order.itemorder_set.all()
    total_price = sum(item.quantity * item.product_id.preu for item in item_orders)

    order.preu_total = total_price
    order.save()

    return Response({
        "message": "Item quantity and order total updated successfully.",
        "new_quantity": item_order.quantity,
        "new_total_price": order.preu_total
    })