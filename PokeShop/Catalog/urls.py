from django.urls import path
from Catalog.views import getProductos, createProducto, create_categoria, list_categorias, update_categoria, delete_categoria

urlpatterns = [
    path('productos/', getProductos, name='get_productos'),
    path('create_producto/', createProducto, name='create_producto'),
    path('categorias/create/', create_categoria, name='create_categoria'),
    path('categorias/', list_categorias, name='list_categorias'),
    path('categorias/update/<int:pk>/', update_categoria, name='update_categoria'), 
    path('categorias/delete/<int:pk/', delete_categoria, name='delete_categoria'),
]
