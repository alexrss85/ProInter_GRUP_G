from django.urls import path
from . import views

urlpatterns = [
    path('categorias/create/', views.create_categoria, name='create_categoria'),
]