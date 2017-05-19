"""
prueba de pydoc
"""

from __future__ import unicode_literals
from django.db import models

class tipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return '{}'.format(self.nombre)

class Mantenimiento (models.Model):

    estado = models.CharField(max_length=50, null=True, blank=True)#a realizar, en curso, terminado
    tipo = models.ForeignKey(tipoMantenimiento, null=True, blank=True, on_delete=models.CASCADE)# preventivo o correctivo
    descripcion = models.CharField(max_length=100)# que le paso al recurso
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    cod_recurso = models.IntegerField(null=True, blank=True)


# Create your models here.
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



class recurso(models.Model):
    """este modelo contiene los datos de un recurso, nombre, estado y tipo"""
    nombre = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadoRecurso, null=True, blank=True, on_delete=models.CASCADE)
    mantenimiento = models.ForeignKey(Mantenimiento, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("ver_recurso", "Puede ver los recursos disponibles"),
        )

