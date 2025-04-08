from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipoDocumento = models.CharField(max_length=10)
    numeroDocumento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    notas = models.TextField(blank=True, null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10, default='Activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
