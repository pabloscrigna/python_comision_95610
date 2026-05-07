from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login


from django.shortcuts import render

from Main.forms import UserRegisterForm

def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username') 
            clave = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)

            if user:
                login(request, user)
                return render(request, "login_respuesta.html", {"mensaje": f"Bienvenido {user}"})
        else:
            return render(request, "login_respuesta.html", {"mensaje": "Error de Autenticación"})
    
    form = AuthenticationForm()

    return render(request, "login.html", {"form": form} )


def registrar_usuario(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()     # creo el usuario en la DB
            return render(request, "login_respuesta.html", {"mensaje": f"Usuario {username} creado!!!"})

    form = UserRegisterForm()

    return render(request, "registro.html", {"form": form })