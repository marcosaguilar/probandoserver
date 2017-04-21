from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mantenimiento(models.Model):
    estado = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

class Tipo_de_recurso(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

class recurso(models.Model):
    estado = models.CharField(max_length=20)
    mantenimiento = models.ForeignKey(Mantenimiento, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)
