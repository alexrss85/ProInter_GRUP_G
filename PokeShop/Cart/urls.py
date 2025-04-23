from django.urls import path
from Cart.views import createCarrito, listCarritos, getCarrito, deleteCarrito, createItemCarrito, listItemsCarrito, getItemCarrito, updateItemCarrito, deleteItemCarrito, getUsers, getUser, createUser, updateUser, deleteUser

urlpatterns = [
    path('carritos/', listCarritos, name='list-carritos'),
    path('carritos/create/', createCarrito, name='create-carrito'),
    path('carritos/<int:pk>/', getCarrito, name='get-carrito'),
    path('carritos/delete/<int:pk>/', deleteCarrito, name='delete-carrito'),
    path('item-carrito/', listItemsCarrito, name='list-items-carrito'),
    path('item-carrito/create/', createItemCarrito, name='create-item-carrito'),
    path('item-carrito/<int:pk>/', getItemCarrito, name='get-item-carrito'),
    path('item-carrito/update/<int:pk>/', updateItemCarrito, name='update-item-carrito'),
    path('item-carrito/delete/<int:pk>/', deleteItemCarrito, name='delete-item-carrito'),
    path('users/', getUsers, name="list-users"),
    path('users/<int:pk>/', getUser, name="get-user"),
    path('users/create/', createUser, name="create-user"),
    path('users/<int:pk>/update/', updateUser, name="update-user"),
    path('users/<int:pk>/delete/', deleteUser, name="delete-user"),
]