from django.db import models
from Cart.models import User
from Catalog.models import Product

class Order(models.Model):
    preu_total = models.IntegerField()  
    estat = models.CharField(max_length=50) 
    id_usuari = models.ForeignKey(User, on_delete=models.CASCADE)  

class ItemOrder(models.Model):
    oder_id = models.ForeignKey(Order, on_delete=models.CASCADE)  
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
