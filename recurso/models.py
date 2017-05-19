"""
prueba de pydoc
"""

from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Mantenimiento(models.Model):
    """contiene los datos del mantenimiento, como la fecha y la descripcion del mismo"""
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()


class EstadoRecurso(models.Model):
    """contiene los estados de un recurso"""
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return '{}'.format(self.estado)


class Tipo_de_recurso(models.Model):
    """contiene los datos de un tipo de recurso, nombre y descripcion"""
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def get_nombre(self):
        return self.nombre


class recurso(models.Model):
    """este modelo contiene los datos de un recurso, nombre, estado y tipo"""
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadoRecurso, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)
    mantenimiento = models.ForeignKey(Mantenimiento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("ver_recurso", "Puede ver los recursos disponibles"),
        )

