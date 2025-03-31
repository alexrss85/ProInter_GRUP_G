from django.urls import path
from Cart.views import createCarrito, listCarritos, getCarrito, updateCarrito, deleteCarrito

urlpatterns = [
    path('carritos/', listCarritos, name='list-carritos'),
    path('carritos/create/', createCarrito, name='create-carrito'),
    path('carritos/<int:pk>/', getCarrito, name='get-carrito'),
    path('carritos/update/<int:pk>/', updateCarrito, name='update-carrito'),
    path('carritos/delete/<int:pk>/', deleteCarrito, name='delete-carrito'),
]