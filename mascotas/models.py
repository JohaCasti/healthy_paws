from django.db import models
from users.models import Person

# Create your models here.
class Mascota(models.Model):
    ESTADO = [
        ('ON', 'Dentro la veterinaria'),
        ('OFF', 'Fuera de la veterinaria'),
    ]
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30, default='animal')
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()
    estado = models.CharField(max_length=3, choices=ESTADO, default='OFF')
    persona = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



"""
relacion muchos a muchos es: ej
authors = models.ManyToManyField(Author, related_name='authors')
relacion uno a uno es: ej
author = models.OneToOneField(Author, on_delete=models.CASCADE)
"""