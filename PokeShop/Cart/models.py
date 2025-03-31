from django.db import models
from Catalog.models import Product

class User(models.Model):
    roles= [('usuario','Usuario'),('admin','Admin')] 
    username = models.CharField(max_length=50)  
    email = models.EmailField(max_length=50) 
    password = models.CharField(max_length=50)
    rol = models.CharField(max_length=20, choices=roles, default='Pendent')


class Carrito(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 

class ItemCarrito(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    quantity = models.IntegerField()