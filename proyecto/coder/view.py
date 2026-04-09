from django.http import HttpResponse
from django.template import Template, Context

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
