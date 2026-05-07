from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoForm, CursoModelForm


def inicio(request):
    return render(request, "index.html")


def cursos(request):

    cursos = Curso.objects.all()
    return render(request, "index_cursos.html", {"cursos": cursos})


def crear_curso(request):

    if request.method == "POST":
        print("request POST: ", request.POST)
        form = CursoModelForm(request.POST)

        if form.is_valid():
            # Crear el curso en la DB
            # nombre = request.POST["nombre"]
            # camada = request.POST["camada"]
            # modalidad = request.POST["modalidad"]
            # if nombre and camada:
            #     Curso.objects.create
            print("datos form: ", form.cleaned_data)
            Curso.objects.create(**form.cleaned_data) 
        else:
            print("error al crear el curso")
            print(form.errors)

        return redirect('cursos')
    # GET
    form = CursoModelForm()
    return render(request, "crear_curso.html", {"form": form})


def editar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        form = CursoModelForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')

    form = CursoModelForm(instance=curso)
    return render(request, "crear_curso.html", {"form": form})


def eliminar_curso(request, id):

    curso = get_object_or_404(Curso, id=id)
    print("curso nombre", curso.nombre)
    curso.delete()
    return redirect('cursos')


def ver_curso(request, id):

    curso = get_object_or_404(Curso, id=id)

    return render(request, "index_cursos.html", {"cursos": [curso]})


class ProfesorListView(ListView):
    model = Profesor
    template_name = "profesores/index_profesores.html"
    context_object_name = 'profesores'


class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = 'profesores/form.html'
    fields = [ 'nombre', 'apellido', 'email', 'profesion' ]
    success_url = reverse_lazy('profesores')


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "profesores/detalle.html"
    context_object_name = 'profesor'


class ProfesorUpdateView(UpdateView):
    model = Profesor
    template_name = "profesores/form.html"
    fields = [ 'nombre', 'apellido', 'email' ]
    success_url = reverse_lazy('profesores')


class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = "profesores/confirm_delete.html"
    success_url = reverse_lazy('profesores')
    

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
