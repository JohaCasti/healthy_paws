from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField() 
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)  # ejemplo: 10.00 para 10%
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # opcional
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Si el stock llega a 0, deshabilitar el producto
        if self.stock <= 0:
            self.habilitado = False
        else:
            self.habilitado = True
        super().save(*args, **kwargs)

