from django.urls import path
from Catalog.views import getProductos, createProducto, create_categoria, list_categorias, update_categoria, delete_categoria, getProducto, updateProducto, deleteProducto, getProductosByCategoria


urlpatterns = [
    path('productos/', getProductos, name='get_productos'),
    path('productos/<int:pk>/', getProducto, name='get_producto'),
    path('productos/create/', createProducto, name='create_producto'),
    path('productos/update/<int:pk>/', updateProducto, name='update_producto'),
    path('productos/delete/<int:pk>/', deleteProducto, name='delete_producto'),
    path('categorias/create/', create_categoria, name='create_categoria'),
    path('categorias/', list_categorias, name='list_categorias'),
    path('categorias/update/<int:pk>/', update_categoria, name='update_categoria'), 
    path('categorias/delete/<int:pk>/', delete_categoria, name='delete_categoria'),
    path('productos/categoria/<str:nom_categoria>/', getProductosByCategoria, name='get_producto_by_categoria'),
]
