from django.urls import path
from Order.views import getOrderByUserAndOrderId,updateOrderStatus,getOrdersByUser, addCartItemsToOrder, deleteItemOrder, deleteOrder, updateItemOrderQuantity

urlpatterns = [
    path('orders/add-items/', addCartItemsToOrder, name='add-items-to-order'),
    path('orders/<int:user_id>/', getOrdersByUser, name='get-orders-by-user'),
    path('orders/itemorder/delete/<int:itemorder_id>/', deleteItemOrder, name='delete-itemorder'),
    path('orders/delete/<int:order_id>/', deleteOrder, name='delete-order'),
    path('orders/<int:order_id>/itemorder/update/<int:itemorder_id>/', updateItemOrderQuantity, name='update-itemorder-quantity'),
    path('orders/<int:order_id>/update-status/', updateOrderStatus, name='update-order-status'),
    path('order/<int:user_id>/<int:order_id>/', getOrderByUserAndOrderId, name='get_order_by_user_and_order'),
]
