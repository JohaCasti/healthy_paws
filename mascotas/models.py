from django.db import models
from users.models import Person
from django.core.validators import MinValueValidator 

# Create your models here.
class Mascota(models.Model):
    ESTADO = [
        ('ON', 'Admision veterinaria | guarderia'),
        ('OFF', 'En casa'),
    ]
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30, default='animal')
    raza = models.CharField(max_length=30)
    edad = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    estado = models.CharField(max_length=3, choices=ESTADO, default='OFF')
    persona = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



"""
relacion muchos a muchos es: ej
authors = models.ManyToManyField(Author, related_name='authors')
relacion uno a uno es: ej
author = models.OneToOneField(Author, on_delete=models.CASCADE)

---------------------------
opcional limitante
ESPECIES = [
    ('perro', 'Perro'),
    ('gato', 'Gato'),
    ('ave', 'Ave'),
    # ...
]
especie = models.CharField(max_length=30, choices=ESPECIES)



"""