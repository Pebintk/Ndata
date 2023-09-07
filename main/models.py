from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()