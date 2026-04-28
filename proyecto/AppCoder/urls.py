from django.urls import path

from AppCoder.views import cursos, inicio, crear_curso


urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("cursos/nuevo/", crear_curso, name="crear_curso")
]
