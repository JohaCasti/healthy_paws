from django import forms
from .models import Mascota

class CreationMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'estado', 'persona']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la mascota', 'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'placeholder': 'Especie', 'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'placeholder': 'Raza', 'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Edad en años', 'class': 'form-control'}),
            'estado': forms.Select(),
            'persona': forms.Select(),
        }