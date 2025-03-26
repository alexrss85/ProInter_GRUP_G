from django.urls import path
from Catalog.views import getProductos, createProducto

urlpatterns = [
    path('productos/', getProductos, name='get_productos'),
    path('create_producto/', createProducto, name='create_producto'),
]
