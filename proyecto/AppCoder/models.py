from django.db import models


# DB --> Tabla Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()


# DB -- Tabla Entregable (Columnas: nombre - fecha - entregado)
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    entregado = models.BooleanField()
