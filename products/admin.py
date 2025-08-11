from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('nombre', 'descripcion', 'precio', 'stock', 'descuento', 'imagen', 'habilitado',)
    search_fields = ['name', 'price']

admin.site.register(Producto, ProductAdmin)