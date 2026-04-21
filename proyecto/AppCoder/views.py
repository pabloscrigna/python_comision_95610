from django.shortcuts import render

from AppCoder.models import Curso


def cursos(request):

    cursos = Curso.objects.all()
    return render(request, "index_cursos.html", {"cursos": cursos})

