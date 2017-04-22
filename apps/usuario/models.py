from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class permiso(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    permisos = models.ManyToManyField(permiso)

    def __unicode__(self):
        return '{}'.format(self.nombre)


class usuario(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=500)
    cedula = models.IntegerField(null=True, blank=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=50)
    rol = models.ManyToManyField(rol)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','cedula']
