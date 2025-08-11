from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    direccion = models.TextField()
    contraseña = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    


    