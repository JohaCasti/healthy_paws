from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from functools import wraps
from .forms import CreationMascota
from .models import Mascota
# Create your views here.

def mascotas(request):

    mascotas = Mascota.objects.filter(persona__user=request.user)

    if request.method == 'POST':
        form = CreationMascota(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Mascota registrada exitosamente!")
            return redirect('mascotas')
        else:
            messages.error(request, "Hubo un error al registrar la mascota. Por favor, revisa los campos.")
    else:
        form = CreationMascota()
    return render(request, 'mascotas.html', {
        'form': form,
        'mascotas': mascotas
    })