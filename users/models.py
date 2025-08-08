from django.db import models

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre