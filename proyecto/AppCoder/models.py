from django.db import models


# DB --> Tabla Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} -- {self.camada}"


# DB -- Tabla Entregable (Columnas: nombre - fecha - entregado)
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"estudiante: {self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    apellido = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    profesion = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f"profesor: {self.apellido}, {self.nombre}"
