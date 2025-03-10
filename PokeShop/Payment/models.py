from django.db import models
from Order.models import Order

# Create your models here.
class Paymeny(models.Model):
    ESTATS = [('pendent','Pendent'),('completat','Completat'),('fallit','Fallit')]  
    num_tarjeta = models.CharField(max_length=16)
    data_caducitat = models.DateField()
    cvc = models.CharField(max_length=3)
    estat_pagament = models.CharField(max_length=20, choices=ESTATS, default='Pendent')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)