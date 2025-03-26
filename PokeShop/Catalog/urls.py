from django.urls import path
from Catalog.views import getProductos, getProducto, createProducto, updateProducto, deleteProducto

urlpatterns = [
    path('productos/', getProductos, name='get_productos'),
    path('productos/<int:pk>/', getProducto, name='get_producto'),
    path('productos/create/', createProducto, name='create_producto'),
    path('productos/<int:pk>/update/', updateProducto, name='update_producto'),
    path('productos/<int:pk>/delete/', deleteProducto, name='delete_producto'),
]
