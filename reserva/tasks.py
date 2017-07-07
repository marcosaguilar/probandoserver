# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from .views import calcular_reserva
from datetime import datetime, timedelta


@shared_task
def reservar():
    for reserva1 in reserva.objects.all():
        if reserva1.fecha_inicio.__str__() <= (datetime.now().date()+timedelta(days=2)):
            calcular_reserva(reserva1.id)
