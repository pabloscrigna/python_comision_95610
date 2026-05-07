from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.shortcuts import render



def saludo(request):
    return HttpResponse("Hola mundo!!!")


def segunda_vista(request):
    return HttpResponse("<br><h1>Mi primera vista!!!</h1>")


def saluda_nombre(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}!!!</h1>")


def prueba_template(request):

    file_template = open("/home/pablo/Documents/coderhouse/python-95610/python_comision_95610/proyecto/coder/templates/index.html")

    # data = file_template.read()
    # template = Template(data)
    template = Template(file_template.read())

    contexto = Context()

    response = template.render(contexto)

    return HttpResponse(response)


def prueba_contexto(request):

    file_template = open("/home/pablo/Documents/coderhouse/python-95610/python_comision_95610/proyecto/coder/templates/index.html")

    template = Template(file_template.read())
    # print("fecha y hora:", datetime.now())
    
    datos_template = {
        "nombre": "Juan",
        "apellido": "Perez",
        "fecha_hora": datetime.now(),
        "productos": {
            "televisor": 2000,
            "heladera": 5000,
        }
    }
    
    contexto = Context(datos_template)

    response = template.render(contexto)

    return HttpResponse(response)


def prueba_loader(request):

    template = loader.get_template("index.html")

    datos_template = {
        "nombre": "Juan",
        "apellido": "Perez",
        "fecha_hora": datetime.now(),
        "productos": {
            "televisor": 90000,
            "heladera": 80000,
        }
    }

    response = template.render(datos_template)
    return HttpResponse(response)



def login_request(request):
    
    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username') 
            clave = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)

            if user:
                login(request, user)
                return HttpResponse("Login exitoso!!!!")

    
    form = AuthenticationForm()

    return render(request, "login.html", {"form": form} )