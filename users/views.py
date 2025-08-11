from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Person

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            persona = Person.objects.get(nombre=username)
            if persona.contraseña == password:
                # Login exitoso, puedes guardar el usuario en la sesión si quieres
                request.session['persona_id'] = persona.id
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('home')  # Asegúrate que exista esta URL
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Person.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
    return render(request, 'login.html')

def contacto(request):
    return render(request, 'contacto.html')

def about(request):
    return render(request, 'about.html')

