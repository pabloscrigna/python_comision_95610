from django.shortcuts import render, redirect

from AppCoder.models import Curso
from AppCoder.forms import CursoForm


def inicio(request):
    return render(request, "index.html")


def cursos(request):

    cursos = Curso.objects.all()
    return render(request, "index_cursos.html", {"cursos": cursos})


def crear_curso(request):

    if request.method == "POST":
        print("request POST: ", request.POST)
        nombre = request.POST["nombre"]
        camada = request.POST["camada"]
        
        # Crear el curso en la DB
        if camada and nombre:
            Curso.objects.create(nombre=nombre, camada=camada) 

        return redirect('cursos')

    form = CursoForm()
    return render(request, "crear_curso.html", {"form": form})



# def crear_curso(request):
# 
#     print("Método: ", request.method)
#     # print("headers: ", request.headers)
#     
#     if request.method == "POST":
#         print("request POST: ", request.POST)
#         nombre = request.POST["nombre"]
#         camada = request.POST["camada"]
# 
#         # Crear el curso en la DB
#         if camada and nombre:
#             Curso.objects.create(nombre=nombre, camada=camada) 
# 
#         return redirect('cursos')
#      
#     # print("request GET:", request.GET)
#     # activo = request.GET["activo"]
#     # activo = request.GET.get("activo", "")
#     # print("activo: ", activo)
#     # estado = request.GET.get("estado", "no definido estado")
#     # print("estado: ", estado)
#     return render(request, "crear_curso.html")
