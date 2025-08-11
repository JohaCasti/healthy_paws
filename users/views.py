from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CreationFormUser
from .models import Person

# Create your views here.
def index(request):

    return render(request, 'index.html')

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Autenticar usuario con el sistema de Django
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usuario autenticado correctamente
            auth_login(request, user)  # Iniciar sesión con Django
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def about(request):
    return render(request, 'about.html')

