from django.contrib import admin
from .models import Producto
# Register your models here.
@admin.register(Producto) #registra en la base de datos el modelo Producto
class AdminProducto(admin.ModelAdmin): #Como se mostrara en el admin
    list_display = ['id', 'name', 'price', 'stock', 'Available']
    list_filter = ['Available']
    