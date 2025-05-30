from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True) 
    category = models.CharField(max_length=100) 
    quantity = models.IntegerField() 
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        pass