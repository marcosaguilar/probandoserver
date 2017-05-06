from __future__ import unicode_literals
from django.db import models


# Create your models here.
class EstadoRecurso(models.Model):
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return '{}'.format(self.estado)


class Tipo_de_recurso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class recurso(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadoRecurso, null=True, blank=True, on_delete=models.CASCADE)
    #mantenimiento = models.ForeignKey(Mantenimiento, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("ver_recurso", "Puede ver los recursos disponibles"),
        )