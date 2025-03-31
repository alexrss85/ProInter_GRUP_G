from django.urls import path
from Order.views import getOrdersByUser, addCartItemsToOrder

urlpatterns = [
    path('orders/add-items/', addCartItemsToOrder, name='add-items-to-order'),
    path('orders/<int:user_id>/', getOrdersByUser, name='get-orders-by-user'),
]
