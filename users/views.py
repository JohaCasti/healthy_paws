from django.contrib.auth import authenticate, logout, login as auth_lo
from django.contrib.auth.decorators import login_required # decorador para vistas que requieren autenticación
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CreationFormUser
from functools import wraps # para crear decoradores personalizados
from .models import Person

# Create your views here.

# Decorador personalizado para vistas públicas
def public_view(origin_view):
    @wraps(origin_view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return origin_view(request, *args, **kwargs)
    return wrapper

@public_view
def index(request):

    return render(request, 'index.html')

@public_view
def registro(request):
    if request.method == 'POST':
        form = CreationFormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Registro exitoso!") # agregar tag , extra_tags ='loque quiero agregar'
            return redirect('login')  # o donde quieras redirigir
        else:
            messages.error(request, "Hubo un error. Por favor, revisa los campos.")
    else:
        form = CreationFormUser()
    return render(request, 'registro.html', {'form': form})

@public_view
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticar usuario con el sistema de Django
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usuario autenticado correctamente
            auth_lo(request, user)  # Iniciar sesión con Django
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')


# def about(request):
#     logout(request)
#     messages.success(request, "Sesión cerrada correctamente.")
#     return render(request, 'index.html')
