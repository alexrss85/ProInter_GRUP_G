from django.urls import path
from . import views

urlpatterns = [
    path('categorias/create/', views.create_categoria, name='create_categoria'),
]
from Catalog.views import getProductos, createProducto

urlpatterns = [
    path('productos/', getProductos, name='get_productos'),
    path('create_producto/', createProducto, name='create_producto'),
]
