from django.contrib import admin
from main.models import Product
# Register your models here.
@admin.register(Product)

class Product(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'amount')
    list_filter = ('description'),