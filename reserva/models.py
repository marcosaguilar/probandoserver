from __future__ import unicode_literals
from recurso.models import recurso, Tipo_de_recurso
from usuario.models import usuario
from django.db import models

# Create your models here.
class estadoReserva(models.Model):
    """este modelo contiene los atributos de un estado de reserva"""
    estado = models.TextField(max_length=50)

    def __unicode__(self):
        return '{}'.format(self.estado)


class listaReserva(models.Model):
    """este modelo contiene los atributos de la lista de reserva"""
    fecha = models.TextField(max_length=50) #solo el dia
    recurso = models.ForeignKey(recurso, null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(self.id)


class reserva(models.Model):
    """este modelo contiene los atributos de una reserva"""
    recurso = models.ForeignKey(recurso, on_delete=models.CASCADE)
    tipo_recurso = models.ForeignKey(Tipo_de_recurso, null=True, blank=True, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE)

    fecha_inicio = models.TextField(max_length=50, blank=True)
    fecha_fin = models.TextField(max_length=50, blank=True)
    estado_reserva = models.ForeignKey(estadoReserva, null=True, blank=True, on_delete=models.CASCADE)
    lista_reserva = models.ForeignKey(listaReserva, null=True, blank=True, on_delete=models.CASCADE)
    gano_reserva = models.IntegerField() #0 indeterminado, 1 no, 2 si
    fechayhora = models.TextField(max_length=50, null=True)

    tipo_reserva = models.TextField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return '{}'.format(self.id)


    class Meta:
        permissions = (
            ("ver_reserva", "Puede ver las reservas disponibles"),
        )

