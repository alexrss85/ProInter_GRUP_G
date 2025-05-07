from django.db import models

# Create your models here.
class Categoria(models.Model):
    nom = models.CharField(max_length=50, unique=True) 
    
#Categoria product
class Product(models.Model):
    nom = models.CharField(max_length=50)  
    descripcio = models.CharField(max_length=50) 
    preu = models.IntegerField()  
    stock = models.IntegerField()  
    nom_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, to_field='nom')
    rating = models.IntegerField()
    img = models.CharField()  
