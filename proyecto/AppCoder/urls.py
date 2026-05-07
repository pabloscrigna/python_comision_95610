from django.urls import path

from AppCoder.views import (
    cursos,
    inicio,
    crear_curso,
    editar_curso,
    eliminar_curso,
    ver_curso,
    ProfesorListView,
    ProfesorCreateView,
    ProfesorDetailView,
    ProfesorUpdateView,
    ProfesorDeleteView,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    
    path("cursos/", cursos, name="cursos"),
    path("cursos/nuevo/", crear_curso, name="crear_curso"),
    path("cursos/editar/<int:id>/", editar_curso, name="editar_curso"),
    path("cursos/eliminar/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path("cursos/ver/<int:id>/", ver_curso, name="ver_curso"),
    path("profesores/", ProfesorListView.as_view(), name='profesores'),
    path("profesores/nuevo/", ProfesorCreateView.as_view(), name="crear_profesor" ),
    path("profesores/ver/<int:pk>", ProfesorDetailView.as_view(), name="ver_profesor" ),
    path("profesores/editar/<int:pk>", ProfesorUpdateView.as_view(), name="editar_profesor" ),
    path("profesores/eliminar/<int:pk>/", ProfesorDeleteView.as_view(), name="eliminar_profesor" ),
]
