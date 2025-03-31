from django.db import models
from Cart.models import User
from Catalog.models import Product

class Order(models.Model):
    preu_total = models.IntegerField()  
    estat = models.CharField(max_length=50) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  

class ItemOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)  
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
