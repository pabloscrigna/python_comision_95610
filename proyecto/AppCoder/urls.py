from django.urls import path

from AppCoder.views import cursos


urlpatterns = [
    path("cursos/", cursos)
]
