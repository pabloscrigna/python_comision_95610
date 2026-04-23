from django.urls import path

from AppCoder.views import cursos, inicio


urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos")
]
